from tqdm import tqdm
import logging
import cv2
import numpy as np
import json
import zipfile
import os

import torch
import torch.distributed as dist
from torch.functional import F
from torchvision.ops import box_iou

from mumovideo.utils.comm import reduce_sum

def evaluate(dataset, predictions, task, visualize_dir=""):
    dataset_name = dataset.__class__.__name__
    logger = logging.getLogger("visr.inference")
    logger.info("Performing {} evaluation (Size: {}).".format(dataset_name, len(dataset)))

    
    
        

    
