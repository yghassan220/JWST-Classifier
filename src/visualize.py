"""
visualize.py
------------
Visualization of JWST images and classification results.
Renders detected sources with morphology labels overlaid
on the original image using proper astronomical conventions.
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import ZScaleInterval


def plot_fits_image(image_data: np.ndarray, title: str = "JWST Image", cmap: str = "inferno"):
    """
    Display a FITS image with proper astronomical scaling.

    Args:
        image_data: 2D numpy array of image pixel values
        title: Plot title
        cmap: Matplotlib colormap name
    """
    pass


def plot_detections(image_data: np.ndarray, catalog):
    """
    Overlay detected source positions on the FITS image.

    Args:
        image_data: 2D numpy array of image pixel values
        catalog: Source catalog from detect.build_catalog()
    """
    pass


def plot_classifications(image_data: np.ndarray, catalog, predictions: list):
    """
    Overlay morphology classification labels on detected sources.

    Args:
        image_data: 2D numpy array of image pixel values
        catalog: Source catalog from detect.build_catalog()
        predictions: List of prediction dicts from classify.predict()
    """
    pass


def plot_cutout_grid(cutouts: list, predictions: list = None, cols: int = 5):
    """
    Display a grid of galaxy cutouts with optional classification labels.

    Args:
        cutouts: List of cutout arrays from detect.extract_cutouts()
        predictions: Optional list of prediction dicts
        cols: Number of columns in the grid
    """
    pass


def save_figure(fig, path: str, dpi: int = 150):
    """
    Save a matplotlib figure to disk.

    Args:
        fig: Matplotlib figure object
        path: Output file path
        dpi: Resolution in dots per inch
    """
    pass


if __name__ == "__main__":
    pass
