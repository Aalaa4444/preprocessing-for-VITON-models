# Openpose
## Description
using human pose estimation models (OpenPose 1.17), This preprocessing step involves detecting key points on the human body to accurately map the clothing onto the person.
OpenPose is open-source tool for real-time multi-person keypoint detection. It provides keypoints for the entire body, including the face, hands, and body joints. The key points detected by OpenPose serve as crucial inputs for generating precise clothing alignment in virtual try-on applications. 

## Steps:
1- download openpose-1.7.0 for cpu from <a href="https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases" target="_blank">here</a> ,after that we need to get main models from <a href="https://www.kaggle.com/datasets/changethetuneman/openpose-model?resource=download" target="_blank">kaggle</a>, After download main models , Structure of models directory should be as follows:

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
