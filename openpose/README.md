# OpenPose
## Overview:
This preprocessing step leverages human pose estimation models, specifically OpenPose 1.7.0, to detect key points on the human body. These key points play a critical role in accurately aligning clothing onto a person in virtual try-on applications. OpenPose is an open-source tool for real-time multi-person keypoint detection, providing detailed key points for the body, face, and hands.

## Prerequisites:
Ensure you have downloaded OpenPose 1.7.0 for CPU from the <a href="https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases" target="_blank">official repository</a> .
Additional models can be downloaded from <a href="https://www.kaggle.com/datasets/changethetuneman/openpose-model?resource=download" target="_blank">kaggle</a>, and they must be arranged into the following directory structure:

### Step 1: Download and Setup Models
After downloading the main models, the structure of your models directory should be as follows:
```bash
models
|-- face 
|   |-- pose_iter_116000.caffemodel
|-- hand
|   |-- pose_iter_102000.caffemodel
|-- pose
|   |-- body
|   |   |-- pose_iter_584000.caffemodel
|   |-- coco
|   |   |-- pose_iter_440000.caffemodel
|   |-- mpi
|   |   |-- pose_iter_160000.caffemodel

```
Ensure that all files are correctly placed in their respective folders.

### Step 2: Run the OpenPose Demo
To execute OpenPose and generate the required keypoints, run the following command:
```bash
bin\OpenPoseDemo.exe --image_dir examples\media --hand --write_images output\ --write_json output\ --disable_blending
```
This command processes the images in the examples/media directory, extracts key points for the hands, and saves the output (both images and JSON files) in the output directory. 
The --disable_blending flag ensures that the output images contain only the key points, without blending them with the original image.

### Step 3: (Optional) Clean Up Example Files
To keep your working directory clean, you can delete the example files from the examples/media folder:
```bash
rm examples/media/*
```
