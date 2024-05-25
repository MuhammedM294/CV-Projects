## Description
This project demonstrates how to detect and track hands in a video stream using MediaPipe and OpenCV. The hand detection and tracking are performed in real-time, with hand landmarks drawn on the detected hands and the frames per second (FPS) displayed on the video feed. The project leverages the MediaPipe package, a framework for building multimodal (video, audio, etc.) applied machine learning pipelines, which provides robust hand detection and tracking capabilities.

## How It Works
1. **Initialize Webcam**: The script initializes the webcam feed.
2. **Setup Hand Detector**: An instance of the HandDetector class is created, which uses MediaPipe for hand detection and tracking.
3. **Capture Frames**: Each frame is captured from the webcam.
4. **Detect Hands**: Hands in the frame are detected, and landmarks are drawn if specified.
5. **Calculate FPS**: The frames per second (FPS) are calculated and displayed on the frame.
6. **Display Result**: The resulting frame with hand landmarks and FPS is displayed in a window.

## Requirements
1. **Python 3.x**
2. **OpenCV**
3. **MediaPipe**
4. **Numpy**

## Usage
To run the hand detection script, ensure you have the required packages installed. The script will start the webcam and display the video feed with detected hand landmarks and FPS.

## Running the Script

To run the script, use the following command:

```bash
python3 main.py

