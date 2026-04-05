"""
classify.py
-----------
Galaxy morphology classification using transfer learning.
Fine-tunes a pretrained CNN on the Galaxy Zoo dataset
and runs inference on detected JWST sources.

Classes:
    0 - Elliptical
    1 - Spiral
    2 - Irregular
"""

import torch
import torch.nn as nn
from torchvision import models, transforms
from torch.utils.data import DataLoader


MORPHOLOGY_CLASSES = {
    0: "Elliptical",
    1: "Spiral",
    2: "Irregular"
}


def build_model(num_classes: int = 3, pretrained: bool = True):
    """
    Build a pretrained ResNet model with a custom classification head.

    Args:
        num_classes: Number of morphology classes
        pretrained: Whether to load ImageNet pretrained weights

    Returns:
        PyTorch model ready for fine-tuning
    """
    pass


def get_transforms(train: bool = True):
    """
    Get image transforms for training or inference.

    Args:
        train: If True, include augmentation transforms

    Returns:
        torchvision Compose transform pipeline
    """
    pass


def train(model, dataloader: DataLoader, epochs: int = 10, lr: float = 1e-4):
    """
    Fine-tune the model on Galaxy Zoo data.

    Args:
        model: PyTorch model from build_model()
        dataloader: DataLoader wrapping Galaxy Zoo dataset
        epochs: Number of training epochs
        lr: Learning rate

    Returns:
        Trained model
    """
    pass


def predict(model, cutouts: list):
    """
    Run inference on a list of galaxy cutouts.

    Args:
        model: Trained PyTorch model
        cutouts: List of image arrays from detect.py

    Returns:
        List of dicts with keys: class_id, class_name, confidence
    """
    pass


def save_model(model, path: str = "models/classifier.pth"):
    """
    Save trained model weights to disk.

    Args:
        model: Trained PyTorch model
        path: Output path for weights file
    """
    pass


def load_model(path: str = "models/classifier.pth", num_classes: int = 3):
    """
    Load saved model weights for inference.

    Args:
        path: Path to saved weights file
        num_classes: Number of morphology classes

    Returns:
        Loaded PyTorch model in eval mode
    """
    pass


if __name__ == "__main__":
    pass
