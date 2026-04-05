# 🔭 JWST Galaxy Morphology Classifier

An end-to-end machine learning pipeline for detecting and classifying galaxy morphologies using real imaging data from the James Webb Space Telescope (JWST). Built as a personal project at the intersection of AI engineering and astrophysics.

---

## Overview

This project pulls publicly available JWST observations from NASA\'s MAST archive, processes raw FITS image data using industry-standard astronomy tools, detects galaxy sources, and classifies their morphological types (spiral, elliptical, irregular) using transfer learning.

The goal is twofold: to build genuine domain expertise in astronomical data science, and to produce a clean, well-documented pipeline that demonstrates applied ML on real scientific data.

---

## Pipeline Stages

### 1. Data Acquisition
Query and download JWST imaging data programmatically via `astroquery` from the MAST (Mikulski Archive for Space Telescopes). Observations are filtered by instrument, filter band, and target field.

### 2. Image Processing
Raw FITS files are opened and preprocessed using `astropy`. This includes background estimation, noise characterization, flux scaling, and proper WCS (World Coordinate System) handling to maintain spatial accuracy.

### 3. Source Detection
Galaxy sources are detected using `photutils` through image segmentation and source cataloging. This stage identifies candidate objects, computes their positions, and extracts cutout stamps for classification.

### 4. Morphology Classification
A pretrained CNN (ResNet / EfficientNet via `torchvision`) is fine-tuned on the Galaxy Zoo dataset — a large collection of human-labeled galaxy morphologies. The trained model is then run on detected JWST sources to predict morphological class.

### 5. Visualization & Output
Results are rendered using `matplotlib` and `astropy.visualization`, with classified sources overlaid on the original JWST image with labeled annotations and confidence scores.

---

## Tech Stack

| Category | Tools |
|---|---|
| Data Access | `astroquery`, MAST Archive |
| FITS Handling | `astropy`, `astropy.io.fits` |
| Image Processing | `photutils`, `scipy.ndimage`, `reproject` |
| Visualization | `matplotlib`, `astropy.visualization`, `WCSAxes` |
| ML / Modeling | `PyTorch`, `torchvision`, `scikit-learn` |
| Environment | Python 3.11+, `uv`, JupyterLab / Cursor |

---

## Project Structure

```
JWST-CLASS/
│
├── data/                   # Local data directory (gitignored)
│   ├── raw/                # Downloaded FITS files
│   └── cutouts/            # Extracted galaxy stamps
│
├── notebooks/              # Exploration and development notebooks
│   ├── 01_data_pipeline.ipynb
│   ├── 02_source_detection.ipynb
│   ├── 03_classification.ipynb
│   └── 04_visualization.ipynb
│
├── src/                    # Clean pipeline scripts
│   ├── download.py         # Data acquisition
│   ├── preprocess.py       # FITS processing
│   ├── detect.py           # Source detection
│   ├── classify.py         # Model inference
│   └── visualize.py        # Output rendering
│
├── models/                 # Saved model weights (gitignored)
├── outputs/                # Classified images and result files
├── pyproject.toml          # Dependencies managed via uv
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- [`uv`](https://github.com/astral-sh/uv) for package management
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/yghassan220/jwst-classifier.git
cd jwst-classifier

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

uv add astropy astroquery photutils matplotlib numpy scipy torch torchvision scikit-learn ipykernel

# Register Jupyter kernel
python -m ipykernel install --user --name=jwst-classifier --display-name "JWST Classifier"
```

### Running the Notebooks

Open the project in Cursor or JupyterLab and run notebooks in order (01 → 04). Each notebook is self-contained with inline explanations.

---

## Data Sources

- **JWST Observations** — [MAST Archive](https://mast.stsci.edu) via `astroquery`
- **Galaxy Zoo Dataset** — Human-labeled galaxy morphologies used for training ([Zenodo](https://zenodo.org/record/3565489))

> ⚠️ Raw FITS files and model weights are not committed to this repository due to size. Download instructions are provided in `notebooks/01_data_pipeline.ipynb`.

---

## Learning Resources

**Astronomy Foundations**
- [OpenStax Astronomy](https://openstax.org/books/astronomy-2e/pages/1-introduction) — Free textbook, focus on galaxy and telescope chapters
- [Crash Course Astronomy](https://www.youtube.com/playlist?list=PL8dPuuaLjXtPAJr1ysd5yGIyiSFuh0mIL) — YouTube series for intuition building

**Applied Tools**
- [Astropy Tutorials](https://learn.astropy.org) — Hands-on notebooks, start with FITS Files and Image Analysis
- [photutils Documentation](https://photutils.readthedocs.io) — Source detection and photometry
- [MAST Archive Notebooks](https://github.com/spacetelescope/mast_notebooks) — Official JWST data access examples

**ML for Astronomy**
- [Galaxy Zoo Paper](https://arxiv.org/abs/0803.0486) — Lintott et al., the foundation of morphology classification
- [Zoobot Library](https://github.com/mwalmsley/zoobot) — Purpose-built galaxy morphology ML, great reference

---

## Author

Built by [Youssef Hassan](https://github.com/yghassan220) AI Engineer with a passion for space science and applied ML.

---

## License

MIT