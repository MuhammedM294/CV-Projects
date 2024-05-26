import time
import math
import warnings
import cv2
import numpy as np
import mediapipe as mp
from handtracking import HandDetector
from utils import set_volume

warnings.filterwarnings("ignore")


def initialize_video_capture(width=1280, height=720):
    """
    Initializes video capture from the default camera with the specified width and height.

    Parameters
    ----------
    width : int, optional
        Width of the video frame (default is 1280).
    height : int, optional
        Height of the video frame (default is 720).

    Returns
    -------
    cv2.VideoCapture
        Initialized video capture object.
    """
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    if not cap.isOpened():
        raise ValueError("Error: Could not open video.")
    return cap


def process_frame(detector, frame, pTime):
    """
    Processes a single frame: detects hands, draws landmarks, calculates FPS, and adjusts volume.

    Parameters
    ----------
    detector : HandDetector
        Instance of HandDetector for detecting hands.
    frame : numpy.ndarray
        The input video frame.
    pTime : float
        Previous time for FPS calculation.

    Returns
    -------
    frame : numpy.ndarray
        The processed frame with landmarks and FPS.
    cTime : float
        Current time for FPS calculation.

    """
    frame = detector.findHands(frame, draw=True)
    lmsList = detector.findPosition(frame, draw=False, handNo=0)

    if len(lmsList) != 0:
        cv2.line(frame, lmsList[4][1:], lmsList[8][1:], (255, 0, 255), 2)
        length = math.hypot(
            lmsList[4][1] - lmsList[8][1], lmsList[4][2] - lmsList[8][2]
        )
        vol = int(np.interp(length, [50, 300], [0, 100]))
        set_volume(f"{vol}%")
        cv2.putText(
            frame,
            f"Volume: {vol}%",
            (95, 100),
            cv2.FONT_HERSHEY_PLAIN,
            2,
            (0, 0, 255),
            2,
        )

        cv2.rectangle(frame, (60, 100), (95, 300), (255, 0, 0), 3)
        cv2.rectangle(frame, (60, 300 - (vol * 2)), (95, 300), (255, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        frame,
        f"FPS: {str(int(fps))}",
        (10, 500),
        cv2.FONT_HERSHEY_PLAIN,
        2,
        (0, 0, 0),
        2,
    )
    return frame, cTime


def main():
    """
    Main function to initialize video capture, hand detector, and process video frames in real-time.
    """
    # Initialize video capture and hand detector
    cap = initialize_video_capture()
    detector = HandDetector()
    pTime = 0

    # Main loop to process video frames
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Cannot receive frame.")
            break

        frame, pTime = process_frame(detector, frame, pTime)
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release video capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
