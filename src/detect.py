"""
detect.py
---------
Galaxy source detection using photutils.
Performs image segmentation, source cataloging,
and cutout extraction for downstream classification.
"""

import numpy as np
from astropy.nddata import Cutout2D


def detect_sources(image_data: np.ndarray, threshold: float = 3.0):
    """
    Detect sources in a preprocessed image using segmentation.

    Args:
        image_data: Background-subtracted 2D image array
        threshold: Detection threshold in units of background RMS

    Returns:
        SegmentationImage of detected sources
    """
    pass


def build_catalog(segmentation, image_data: np.ndarray):
    """
    Build a source catalog from segmentation results.

    Args:
        segmentation: SegmentationImage from detect_sources()
        image_data: Original image array

    Returns:
        Astropy Table of source properties (position, flux, shape)
    """
    pass


def extract_cutouts(catalog, image_data: np.ndarray, size: int = 64):
    """
    Extract fixed-size image cutouts around each detected source.

    Args:
        catalog: Source catalog from build_catalog()
        image_data: Original image array
        size: Cutout size in pixels (size x size)

    Returns:
        List of 2D numpy arrays, one per source
    """
    pass


def save_cutouts(cutouts: list, output_dir: str = "data/cutouts"):
    """
    Save extracted cutouts to disk for classification.

    Args:
        cutouts: List of cutout arrays from extract_cutouts()
        output_dir: Directory to save cutout files
    """
    pass


if __name__ == "__main__":
    pass
