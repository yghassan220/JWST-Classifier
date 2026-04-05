"""
download.py
-----------
Data acquisition from NASA's MAST archive via astroquery.
Handles querying JWST observations and downloading FITS files.
"""

from astroquery.mast import Observations


def query_jwst_observations(filters: str = "F200W", limit: int = 10):
    """
    Query JWST observations from MAST archive.

    Args:
        filters: JWST filter band to query (e.g. F200W, F090W)
        limit: Maximum number of observations to return

    Returns:
        Astropy Table of matching observations
    """
    pass


def get_products(observation):
    """
    Get downloadable products for a given observation.

    Args:
        observation: Single observation row from query results

    Returns:
        Astropy Table of available products
    """
    pass


def download_fits(products, output_dir: str = "data/raw"):
    """
    Download FITS files for given products.

    Args:
        products: Product table from get_products()
        output_dir: Local directory to save downloaded files

    Returns:
        List of downloaded file paths
    """
    pass


if __name__ == "__main__":
    obs = query_jwst_observations()
    products = get_products(obs[0])
    download_fits(products)
