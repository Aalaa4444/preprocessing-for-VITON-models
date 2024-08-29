import os, sys
import cv2
from PIL import Image
import numpy as np
import json
import shutil
# image_parse------------------------------------------------------------------------
imgforHD=cv2.imread("test_img.jpg")
ori_imgHD=cv2.resize(imgforHD,(768,1024))
cv2.imwrite("./image_parse/image_segmentation/input/0.jpg",ori_imgHD)
print("Running human part segmentation scripts\n")
os.chdir("./image_parse/image_segmentation")
os.system("python human_part_segmentation.py")
os.system("python human_part_segmentation.py --arch lip --savepath ./output/1.png")
os.system("python palette.py")
os.chdir("../../")  # Adjust based on your project's directory structure
imgfor_HDseg=cv2.imread("./image_parse/image_segmentation/output/0.png")
imgfor_HDseg=cv2.resize(imgfor_HDseg,(768,1024))
cv2.imwrite("./image_parse.png",imgfor_HDseg)

# openpose---------------------------------------------------------------------------
imgforHD=cv2.imread("test_img.jpg")
ori_imgHD=cv2.resize(imgforHD,(768,1024))
cv2.imwrite("./openpose-1.7.0-binaries-win64-cpu-python3.7-flir-3d/examples/media/openpose.jpg",ori_imgHD)
os.chdir("./openpose-1.7.0-binaries-win64-cpu-python3.7-flir-3d")
os.system("bin\OpenPoseDemo.exe --image_dir examples\media --hand --write_images output\ --write_json output\ --disable_blending")
os.remove("./examples/media/openpose.jpg")
os.chdir("../")  # Adjust based on your project's directory structure


imgfor_HDseg=cv2.imread("./openpose-1.7.0-binaries-win64-cpu-python3.7-flir-3d/output/openpose_rendered.png")
cv2.imwrite("./openpose.png",imgfor_HDseg)
os.remove("./openpose-1.7.0-binaries-win64-cpu-python3.7-flir-3d/output/openpose_rendered.png")

# Original JSON file path
original_json_path = "./openpose-1.7.0-binaries-win64-cpu-python3.7-flir-3d/output/openpose_keypoints.json"

# Move the JSON file to the new directory
shutil.move(original_json_path, os.path.join("./openpose_keypoints.json"))

# densepose--------------------------------------------------------------------------

