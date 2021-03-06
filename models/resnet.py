from backbones.resnet import *
from heads.metrics import *
import torch.nn as nn
import numpy as np


class ResNet(nn.Module):
    def __init__(self, num_classes):
        super(ResNet,self).__init__()
        self.num_classes = num_classes
        self.backbone = ResNet50()
        self.head = Softmax(512, num_classes)
    
    def forward(self, x, labels):
        out = self.backbone(x)
        out = self.head(out)
        return out

