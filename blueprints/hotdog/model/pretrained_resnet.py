import torch
from torchvision import models, transforms
import sys
import os


class Hotdog_Model_Resnet():

    def __init__(self):
        self.model = models.resnet101(pretrained=True)
        self.transform = transforms.Compose([
                            transforms.Resize(256),
                            transforms.CenterCrop(224),
                            transforms.ToTensor(),
                            transforms.Normalize(
                                mean=[0.485, 0.456, 0.406],
                                std=[0.229, 0.224, 0.225]
                            )
                        ])
        # sys.path[0] is the location of app.py, or where the script was invoked
        with open(os.path.join(sys.path[0],"blueprints/hotdog/model/imagenet_classes.txt"), "r") as f:
            self.categories = [s.strip() for s in f.readlines()]
            print(len(self.categories))

        self.HOTDOG_CLASS = 934

