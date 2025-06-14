import torch
import torch.nn
import torch.nn.functional as F
from .sh import eval_sh_bases
import numpy as np
import time
import hashlib

'''
def positional_encoding(positions, freqs):

        freq_bands = (2**torch.arange(freqs).float()).to(positions.device)  # (F,)
        pts = (positions[..., None] * freq_bands).reshape(
            positions.shape[:-1] + (freqs * positions.shape[-1], ))  # (..., DF)
        pts = torch.cat([torch.sin(pts), torch.cos(pts)], dim=-1)
        return pts
'''



def hash_position_encoding(positions, num_bins=512):
    """
    使用哈希位置编码对输入位置进行编码。
    参数:
    positions: 输入的空间坐标，形状为 (N, 3) 或 (N, D)
    num_bins: 哈希表的大小

    返回：
    哈希编码后的结果
    """
    encoded_positions = []
    for pos in positions:
        encoded_pos = []
        for dim in pos:
            # 使用哈希函数对每个维度进行编码
            hash_value = int(hashlib.sha256(str(dim.item()).encode('utf-8')).hexdigest(), 16) % num_bins
            encoded_pos.append(hash_value)
        encoded_positions.append(encoded_pos)
    return torch.tensor(encoded_positions, device=positions.device)

def positional_encoding(positions, freqs, use_hash_encoding=False):
    if use_hash_encoding:
        # 使用哈希位置编码
        return hash_position_encoding(positions, num_bins=freqs)
    else:
        # 使用传统的频率编码
        freq_bands = (2**torch.arange(freqs).float()).to(positions.device)
        pts = (positions[..., None] * freq_bands).reshape(
            positions.shape[:-1] + (freqs * positions.shape[-1], ))  # (..., DF)
        pts = torch.cat([torch.sin(pts), torch.cos(pts)], dim=-1)
        return pts


