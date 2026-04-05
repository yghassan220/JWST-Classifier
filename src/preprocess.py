"""
preprocess.py
-------------
FITS image preprocessing using astropy.
Handles file loading, background estimation, flux scaling,
and WCS handling for spatial accuracy.
"""

from astropy.io import fits
from astropy.visualization import ZScaleInterval
import numpy as np


def load_fits(filepath: str):
    """
    Open and load a FITS file.

    Args:
        filepath: Path to the .fits file

    Returns:
        Tuple of (image_data, header, wcs)
    """
    pass


def estimate_background(image_data: np.ndarray):
    """
    Estimate and subtract image background.

    Args:
        image_data: 2D numpy array of image pixel values

    Returns:
        Background-subtracted image array
    """
    pass


def scale_image(image_data: np.ndarray):
    """
    Apply ZScale normalization for display and processing.

    Args:
        image_data: 2D numpy array of image pixel values

    Returns:
        Tuple of (vmin, vmax) scaling limits
    """
    pass


def preprocess_pipeline(filepath: str):
    """
    Run full preprocessing pipeline on a single FITS file.

    Args:
        filepath: Path to raw .fits file

    Returns:
        Processed image data ready for source detection
    """
    pass


if __name__ == "__main__":
    pass
