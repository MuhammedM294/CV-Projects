## Description
This project demonstrates how to detect a specific color in a video stream using OpenCV. The color detection is performed in the HSV color space, which is more robust for color detection tasks compared to the RGB color space.

## How It Works
1. **Initialize Webcam**: The script initializes the webcam feed.
2. **Convert Frame to HSV**: Each frame captured from the webcam is converted from the BGR color space (used by OpenCV) to the HSV color space.
3. **Define Color Range**: The user specifies an RGB color to detect. This RGB color is converted to an HSV range with a specified tolerance.
4. **Create Mask**: A mask is created to isolate the specified color within the HSV range.
5. **Draw Bounding Boxes**: Bounding boxes are drawn around the detected areas in the original frame.
6. **Display Result**: The resulting frame with bounding boxes is displayed in a window.

## Requirements
**1. Python 3.x** 

**2. OpenCV**

**3. Numpy**

**4. Pillow(PIL)**


## Usage
To run the color detection script, ensure you have the required packages installed. You can specify the color you want  in **RGB** format (red, green, blue) to detect using command-line arguments.

## Running the Script

To run the script with a specific color, use the following command format:

```bash
python3 main.py --r <red_value> --g <green_value> --b <blue_value>
```

For example, to detect a pure blue color:

```bash
python3 main.py --r 0 --g 0 --b 255
```




