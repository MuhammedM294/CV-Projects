import cv2
import time

from handtracking import HandDetector


def main():
    """
    Captures video from the default camera, detects hands in real-time, and displays the video with hand landmarks and FPS.

    This main function initializes the camera, sets the frame size, and uses the HandDetector class to find and draw hand landmarks.
    It also calculates and displays the frames per second (FPS) on the video.

    Press 'q' to exit the video window.
    """
    # Initialize video capture from the default camera
    cap = cv2.VideoCapture(0)

    # Set the width and height of the video frame
    cap.set(3, 1280)  # Width
    cap.set(4, 720)  # Height

    # Initialize current and previous time for FPS calculation
    cTime = 0
    pTime = 0

    # Create an instance of HandDetector
    detector = HandDetector()

    # Check if the video capture has been initialized correctly
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Loop to continuously get frames from the camera
    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()

        # Check if the frame was read correctly
        if not ret:
            print("Error: Could not read frame.")
            break

        # Detect hands in the frame and get landmark positions
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame, draw=False)

        # Calculate FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # Display FPS on the frame
        cv2.putText(
            frame,
            f"FPS: {int(fps)}",
            (10, 70),
            cv2.FONT_HERSHEY_PLAIN,
            3,
            (255, 0, 255),
            3,
        )

        # Show the frame with detected hand landmarks and FPS
        cv2.imshow("Camera", frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
