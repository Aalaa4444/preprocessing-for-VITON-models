# OpenPose
## Overview:
This preprocessing step leverages human pose estimation models, specifically OpenPose 1.7.0, to detect key points on the human body. These key points play a critical role in accurately aligning clothing onto a person in virtual try-on applications. OpenPose is an open-source tool for real-time multi-person keypoint detection, providing detailed key points for the body, face, and hands.

## Prerequisites:
Ensure you have downloaded OpenPose 1.7.0 for CPU from the <a href="https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases" target="_blank">official repository</a> .
Additional models can be downloaded from <a href="https://www.kaggle.com/datasets/changethetuneman/openpose-model?resource=download" target="_blank">kaggle</a>, and they must be arranged into the following directory structure:

```bash
models
|-- face 
    |-- pose_iter_116000.caffemodel
    |-- ...

|-- hand
    |-- pose_iter_102000.caffemodel
    |-- ...

|-- pose
    |-- body
        |-- pose_iter_584000.caffemodel
        |-- ...
    |-- coco
        |-- pose_iter_440000.caffemodel
        |-- ...
    |-- mpi
        |-- pose_iter_160000.caffemodel
        |-- ...
|-- ...
```

2- then we can get result using this script:
```bash
bin\OpenPoseDemo.exe --image_dir examples\media --hand --write_images output\ --write_json output\ --disable_blending
```
3- optional: delete all examples that in folder examples\media
