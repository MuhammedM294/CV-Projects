import cv2
import mediapipe as mp


class HandDetector:
    """
    A class to detect and track hands in video frames using MediaPipe.

    Attributes
    ----------
    mode : bool
        Whether to treat input images as static or video stream.
    maxHands : int
        Maximum number of hands to detect.
    detectionCon : float
        Minimum confidence value for hand detection.
    trackCon : float
        Minimum confidence value for hand tracking.
    """

    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        """
        Initializes the HandDetector with the given parameters.

        Parameters
        ----------
        mode : bool, optional
            Whether to treat input images as static or video stream (default is False).
        maxHands : int, optional
            Maximum number of hands to detect (default is 2).
        detectionCon : float, optional
            Minimum confidence value for hand detection (default is 0.5).
        trackCon : float, optional
            Minimum confidence value for hand tracking (default is 0.5).
        """
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon,
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.results = None

    def findHands(self, frame, draw=True):
        """
        Detects hands in the provided frame.

        Parameters
        ----------
        frame : numpy.ndarray
            The input frame in which hands are to be detected.
        draw : bool, optional
            Whether to draw landmarks on the detected hands (default is True).

        Returns
        -------
        numpy.ndarray
            The frame with landmarks drawn if draw is True.
        """
        frmRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(frmRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        frame, handLms, self.mpHands.HAND_CONNECTIONS
                    )
        return frame

    def findPosition(self, frame, handNo=0, draw=True):
        """
        Finds the positions of landmarks in the detected hands.

        Parameters
        ----------
        frame : numpy.ndarray
            The input frame in which hand landmarks are to be found.
        handNo : int, optional
            The index of the hand for which landmarks are to be found (default is 0).
        draw : bool, optional
            Whether to draw circles on the detected landmarks (default is True).

        Returns
        -------
        list of list
            A list of landmark positions where each position is a list [id, cx, cy].
        """
        lmList = []
        if self.results and self.results.multi_hand_landmarks:
            try:
                myHand = self.results.multi_hand_landmarks[handNo]
                h, w, _ = frame.shape
                for id, lm in enumerate(myHand.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(frame, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            except IndexError:
                print(f"Hand number {handNo} not found.")
        return lmList
