import cv2
import argparse
from PIL import Image
from utils import get_hsv_range_from_rgb


def detect_color(source=0, color=(0, 0, 255)):
    """
    Detect the specified color in the webcam feed and draw a bounding box around it.

    params:
    -------

    Source: int or str
        The source of the webcam feed. Default is 0 for the default camera. for a video file, specify the path to the file.

    color: tuple
        The RGB color to detect in the webcam feed.

    returns:
    --------

    None

    """
    # Initialize the webcam feed. 0 is the default camera
    vid = cv2.VideoCapture(source)

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
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Get HSV range for the specified color
        lower, upper = get_hsv_range_from_rgb(*color, tolerance=10)

        # Perform color masking
        mask = cv2.inRange(hsv_frame, lower, upper)

        # Convert mask to PIL Image and find bounding box
        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()

        # Draw bounding box around detected color
        if bbox:
            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 0), 2)

        # Show the frame
        cv2.imshow("frame", frame)

        # Exit if 'x' key is pressed
        if cv2.waitKey(1) == ord("x"):
            break

    # Release the video feed
    vid.release()

    # Close all the windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Detect a specific color in the webcam feed."
    )
    parser.add_argument(
        "--source",
        type=str,
        default=0,
        help="The source of the webcam feed. Default is 0 for the default camera.",
    )
    parser.add_argument(
        "--r", type=int, default=0, help="Red component of the color (0-255)"
    )
    parser.add_argument(
        "--g", type=int, default=0, help="Green component of the color (0-255)"
    )
    parser.add_argument(
        "--b", type=int, default=255, help="Blue component of the color (0-255)"
    )

    args = parser.parse_args()

    # Define the RGB color values to detect from command-line arguments
    color_to_detect = (args.r, args.g, args.b)

    # Call the detect_color function with the specified color
    detect_color(color=color_to_detect)
