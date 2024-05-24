import cv2
import numpy as np


def get_hsv_range_from_rgb(
    r,
    g,
    b,
    tolerance=10,
    min_saturation=100,
    max_saturation=255,
    min_value=100,
    max_value=255,
):
    """
    Convert RGB color to HSV range with given tolerance and saturation/value thresholds.

    params:
    -------

    r: int
        The red value of the RGB color.

    g: int
        The green value of the RGB color.

    b: int
        The blue value of the RGB color.

    tolerance: int
        The tolerance for the hue value in the HSV color space.

    min_saturation: int
        The minimum saturation value for the HSV color.

    min_value: int
        The minimum value for the HSV color.

    max_value: int
        The maximum value for the HSV color.

    returns:
    --------

    lower_bound: np.array
        The lower bound of the HSV range.

    upper_bound: np.array
        The upper bound of the HSV range.

    """
    # Ensure RGB values are within valid range
    r = np.clip(r, 0, 255)
    g = np.clip(g, 0, 255)
    b = np.clip(b, 0, 255)

    # Convert the RGB color to a numpy array
    rgb_color = np.uint8([[[b, g, r]]])

    # Convert the RGB color to HSV using OpenCV
    hsv_color = cv2.cvtColor(rgb_color, cv2.COLOR_BGR2HSV)
    h = hsv_color[0][0][0]

    # Calculate the lower and upper bounds with the given tolerance
    lower_bound = np.array([max(h - tolerance, 0), min_saturation, min_value])
    upper_bound = np.array([min(h + tolerance, 179), max_saturation, max_value])

    return lower_bound, upper_bound


if __name__ == "__main__":
    # Example usage

    lower, upper = get_hsv_range_from_rgb(*(255, 0, 0), tolerance=10)

    print("Lower HSV:", lower)
    print("Upper HSV:", upper)
