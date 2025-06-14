# Enhancing-Novel-View-Synthesis-with-Adaptive-Random-Patch-Radiance-Fields

This repository contains the implementation of the method described in the paper "Enhancing Novel View Synthesis with Adaptive Random Patch Radiance Fields".

## Installation
 
#### Tested on Ubuntu 20.04 + Pytorch 1.10.1 

Install environment:
```
python=3.8
pip install torch torchvision
pip install tqdm scikit-image opencv-python configargparse lpips imageio-ffmpeg kornia lpips tensorboard
```
## Dataset
* [Synthetic-NeRF](https://drive.google.com/drive/folders/128yBriW1IG_3NJ5Rp7APSTZsJqdJdfc1) 
* [Synthetic-NSVF](https://dl.fbaipublicfiles.com/nsvf/dataset/Synthetic_NSVF.zip)
* [Tanks and Temples Advanced Scenes dataset](https://s3.eu-central-1.amazonaws.com/avg-projects/monosdf/data/tnt_advanced.tar)

## How to Run
The training script is in `train.py`, to train a RPRF:

```
python train.py --config configs/lego.txt
```