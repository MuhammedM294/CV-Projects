## Description
This project demonstrates how to detect a specific color in a video stream using OpenCV. The color detection is performed in the HSV color space, which is more robust for color detection tasks compared to the RGB color space.

## How It Works
1. **Initialize Webcam**: The script initializes the webcam feed.
2. **Convert Frame to HSV**: Each frame captured from the webcam is converted from the BGR color space (used by OpenCV) to the HSV color space.
3. **Define Color Range**: The user specifies an RGB color to detect. This RGB color is converted to an HSV range with a specified tolerance.
4. **Create Mask**: A mask is created to isolate the specified color within the HSV range.
5. **Find Contours**: Contours are found within the mask to identify the areas where the specified color is detected.
6. **Draw Bounding Boxes**: Bounding boxes are drawn around the detected areas in the original frame.
7. **Display Result**: The resulting frame with bounding boxes is displayed in a window.

### Usage
To run the color detection script, ensure you have OpenCV and numpy installed. You can specify the color you want to detect by changing the `color_to_detect` variable.
