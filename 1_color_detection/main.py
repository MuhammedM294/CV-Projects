import cv2
import numpy as np
from PIL import Image
from utils import get_hsv_range_from_rgb


def detect_color(color=(0, 0, 255)):
    """
    Detect the specified color in the webcam feed and draw a bounding box around it.

    params:
    -------

    color: tuple
        The RGB color to detect in the webcam feed.

    returns:
    --------

    None

    """
    # Initialize the webcam feed. 0 is the default camera
    vid = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not vid.isOpened():
        print("Error: Could not open webcam.")
        exit()

    while True:
        # Read the video feed
        ret, frame = vid.read()

        # Check if the frame is empty
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Convert frame to HSV color space
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Get HSV range for the specified color
        lower, upper = get_hsv_range_from_rgb(*color, tolerance=10)

        # Perform color masking
        mask = cv2.inRange(frame, lower, upper)

        # Convert mask to PIL Image and find bounding box
        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()

        # Draw bounding box around detected color
        if bbox:
            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 0), 2)

        # Convert frame back to BGR for display
        frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)

        # Show the frame
        cv2.imshow("frame", frame)

        # Exit if 'x' key is pressed
        if cv2.waitKey(1) == ord("x"):
            break

    # Release the video feed
    vid.release()

    # Close all the windows
    cv2.destroyAllWindows()


# Define the RGB color values to detect the color
color_to_detect = (0, 0, 255)


if __name__ == "__main__":
    # Call the detect_color function with the specified color
    detect_color(color_to_detect)
