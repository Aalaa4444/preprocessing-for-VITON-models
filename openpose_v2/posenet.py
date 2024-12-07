import torch
import numpy as np
import cv2
from posenet.models.model_factory import load_model
from posenet.decode_multi import decode_multiple_poses
import json

# Load PoseNet model
net = load_model(101)
net = net.cuda()
output_stride = net.output_stride

# Read image
testfile = "test_img.jpg"
input_image = cv2.imread(testfile)
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# Ensure image is float32 and normalize
input_image = input_image.astype(np.float32) / 255.0

# Prepare image tensor for PoseNet
input_image = torch.Tensor(input_image).permute(2, 0, 1).unsqueeze(0).cuda()

# Run PoseNet inference
with torch.no_grad():
    heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = net(input_image)

# Decode poses
pose_scores, keypoint_scores, keypoint_coords = decode_multiple_poses(
    heatmaps_result.squeeze(0),
    offsets_result.squeeze(0),
    displacement_fwd_result.squeeze(0),
    displacement_bwd_result.squeeze(0),
    output_stride=output_stride,
    max_pose_detections=1,  # Assuming only one person in the image
    min_pose_score=0.15     # Adjust as needed
)

# Get keypoints of the highest scoring pose
if len(pose_scores) > 0 and np.any(pose_scores > 0.1):
    pose_id = np.argmax(pose_scores)
    keypoints = keypoint_coords[pose_id]

    # Map keypoints to OpenPose format
    keypoints_openpose = []
    for i in range(len(keypoints)):
        keypoint = keypoints[i]
        keypoints_openpose.extend([float(keypoint[1]), float(keypoint[0]), keypoint_scores[pose_id][i]])

    # Create JSON data
    data = {
        "version": 1.3,
        "people": [
            {
                "person_id": [-1],  # Assuming one person without ID
                "pose_keypoints_2d": keypoints_openpose,
                "face_keypoints_2d": [],  # Placeholder for face keypoints
                "hand_left_keypoints_2d": [],  # Placeholder for left hand keypoints
                "hand_right_keypoints_2d": []  # Placeholder for right hand keypoints
            }
        ]
    }

    # Save JSON data to file
    output_json_file = '00001_00_keypoints.json'
    with open(output_json_file, 'w') as f:
        json.dump(data, f)

    print(f"JSON file saved: {output_json_file}")
else:
    print("No valid poses found.")

# Display or save the image with keypoints (optional)
# Dense Pose Image Creation (if needed)

# Display or save dense pose image (optional)

