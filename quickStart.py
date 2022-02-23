#基本模型 from tutorials
import imp
import torch
from torch import nn
# torch.utils.data.Dataset和torch.utils.data.DataLoader是pytorch的两大关键原语
# Dataset存储样本和对应标签，DataLoader将Dataset包装成一个可迭代的对象
from torch.utils.data import DataLoader
# torchvision.datasets包含很多真实世界的数据集如CIFAR、COCO
# 本例中使用FashionMNIST数据集
# 每个torchvision的数据集都包含两个参数，transform和target_transform，分别修改样本和标签。
from torchvision import datasets
from torchvision.transforms import ToTensor

