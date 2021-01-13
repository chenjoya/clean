import os
from os.path import join
import json
import cv2
import numpy as np

import torch
from torchvision import transforms

class ViSR(torch.utils.data.Dataset):

    def __init__(self, data, label):
        pass
        
    def __getitem__(self, idx):
        pass

    def __len__(self):
        pass
    
    def visualize(self, sbboxes, scats, ubboxes, upreds, obboxes, ocats, idx):
        pass
        