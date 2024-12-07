import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import json
import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_openpose_image(json_data, img):
    """Create a openpose image from keypoints in JSON data and an image."""
    img_h, img_w, _ = img.shape

    if json_data['people']:
        keypoints = np.array(json_data['people'][0]['pose_keypoints_2d']).reshape(-1, 3)
    else:
        print("json_data is empty")
        return None

    # Create a blank segmentation image with the same dimensions as the original image
    seg_img = np.zeros((img_h, img_w, 3), dtype=np.uint8)

    # Define connections and create a colormap
    connections = [
        (0, 1), (1, 3), (0, 2), (2, 4),  # Nose to eyes and ears
        (5, 6),  # Shoulders
        (5, 7), (7, 9), (6, 8), (8, 10),  # Shoulders to elbows and wrists
        (11, 12),  # Hips
        (11, 13), (13, 15), (12, 14), (14, 16)  # Hips to knees and ankles
    ]

    # Create a colormap with a gradient
    cmap = plt.get_cmap('rainbow')
    num_colors = len(connections) + 2  # Adding 2 for the additional connections
    colors = [cmap(i / num_colors)[:3] for i in range(num_colors)]
    colors = [(int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

    # Draw lines between keypoints to represent the body
    for idx, (start, end) in enumerate(connections):
        if start < keypoints.shape[0] and end < keypoints.shape[0]:
            if keypoints[start][2] > 0 and keypoints[end][2] > 0:  # Only consider connections with non-zero confidence
                start_point = (int(keypoints[start][0]), int(keypoints[start][1]))
                end_point = (int(keypoints[end][0]), int(keypoints[end][1]))

                # Calculate the gradient color for the connection
                color = colors[idx]
                cv2.line(seg_img, start_point, end_point, color, 2)

    # Calculate middle points
    if keypoints[5][2] > 0 and keypoints[6][2] > 0:  # Shoulders
        middle_shoulder = (
            int((keypoints[5][0] + keypoints[6][0]) / 2),
            int((keypoints[5][1] + keypoints[6][1]) / 2)
        )
        if keypoints[0][2] > 0:  # Nose
            cv2.line(seg_img, (int(keypoints[0][0]), int(keypoints[0][1])), middle_shoulder, colors[-2], 2)

    if keypoints[11][2] > 0 and keypoints[12][2] > 0:  # Hips
        middle_hip = (
            int((keypoints[11][0] + keypoints[12][0]) / 2),
            int((keypoints[11][1] + keypoints[12][1]) / 2)
        )
        cv2.line(seg_img, middle_shoulder, middle_hip, colors[-1], 2)

    # Draw keypoints on the segmentation image
    for idx, (x, y, confidence) in enumerate(keypoints):
        if confidence > 0:  # Only consider keypoints with non-zero confidence
            x, y = int(x), int(y)
            color = colors[idx % len(colors)]
            cv2.circle(seg_img, (x, y), 5, color, thickness=-1)

    # Generate the bounding box based on keypoints
    valid_keypoints = keypoints[keypoints[:, 2] > 0][:, :2]
    x_min, y_min = np.min(valid_keypoints, axis=0).astype(int)
    x_max, y_max = np.max(valid_keypoints, axis=0).astype(int)
    w, h = x_max - x_min, y_max - y_min

    # Create the final segmentation image
    bg = np.zeros((img_h, img_w, 3), dtype=np.uint8)
    bg[y_min:y_min+h, x_min:x_min+w, :] = seg_img[y_min:y_min+h, x_min:x_min+w, :]

    return bg  # Return as NumPy array

# Example usage
# Read the input image
input_user_image = cv2.imread('test_img.jpg')

# Read the OpenPose JSON data
with open('00001_00_keypoints.json', 'r') as f:
    openpose_json = json.load(f)

# Resize the input image
ori_img = cv2.resize(input_user_image, (768, 1024))

# Create the DensePose image using the provided function
densepose_image = create_openpose_image(openpose_json, ori_img)

# Save the DensePose image to a file
cv2.imwrite('00001_00_rendered.png', densepose_image)
