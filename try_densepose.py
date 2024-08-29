import os, sys
import cv2
from PIL import Image
import numpy as np
    # Run human part segmentation scripts from person-seg module
imgforHD=cv2.imread("test_img.jpg")
ori_imgHD=cv2.resize(imgforHD,(768,1024))
cv2.imwrite("./densepose/image_segmentation/input/0.jpg",ori_imgHD)
print("Running human part segmentation scripts\n")
os.chdir("./densepose/image_segmentation")
os.system("python human_part_segmentation.py")
os.system("python human_part_segmentation.py --arch lip --savepath ./output/1.png")
os.system("python palette.py")
os.chdir("../../../")  # Adjust based on your project's directory structure
imgfor_HDseg=cv2.imread("./densepose/image_segmentation/output/0.png")
imgfor_HDseg=cv2.resize(imgfor_HDseg,(768,1024))
cv2.imwrite("./densepose.png",imgfor_HDseg)