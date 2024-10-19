# preprocessing-for-VITON-models
## 1- Cloth mask
code uses a pre-trained segmentation model (U-net) and an input image.
It preprocesses the image for the model.
* Preprocessing the image: 
Pads the image to ensure its dimensions are divisible by 32, which is necessary for the models that we will use.
* Preparing Input for Model Inference: 
After setting up an albumentations transformation pipeline for normalization, we apply the normalization transformation to the padded image, then convert the normalized image to a PyTorch tensor and add a batch dimension.
Performs inference using the pre-trained model to obtain a segmentation mask.
* Postprocessing the segmentation mask: It converts the model's output to a binary mask, removes padding from the mask, and then resizes the masked image.
<p align="middle">     
    <img src="https://github.com/Aalaa4444/preprocessing-for-VITON-models/blob/main/cloth_mask/cloth.jpg" width="200">     
    <img src="https://github.com/Aalaa4444/preprocessing-for-VITON-models/blob/main/cloth_mask/cloth-mask.jpg" width="200">    
</p>

## 2- image-parse-v3

## 3- Openpose
## 4- DensePose
