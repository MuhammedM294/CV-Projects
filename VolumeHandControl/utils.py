import subprocess


def set_volume(volume):
    """
    Set the system volume on Ubuntu.

    Parameters:
    ----------

    volume : str
        The volume to set in the format "0%" to "100%".

    Returns:
    -------

    None
    """
    try:
        # Use pactl to set the volume
        subprocess.run(
            ["pactl", "set-sink-volume", "@DEFAULT_SINK@", volume], check=True
        )
        print(f"Volume set to {volume}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set volume: {e}")
