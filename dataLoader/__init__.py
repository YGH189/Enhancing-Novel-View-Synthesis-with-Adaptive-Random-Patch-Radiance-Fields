
from .blender import BlenderDataset
from .nsvf import NSVF
from .tankstemple import TanksTempleDataset




dataset_dict = {'blender': BlenderDataset,
               'tankstemple':TanksTempleDataset,
               'nsvf':NSVF}