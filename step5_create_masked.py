"""
Step 5: Apply a letter mask to a stippled image to simulate selection bias.
Pixels inside the letter region are erased (set to white), removing stipple
dots in a systematic pattern — the visual metaphor for selection bias.
"""

import numpy as np


def create_masked_stipple(
    stipple_img: np.ndarray,
    mask_img: np.ndarray,
    threshold: float = 0.5,
) -> np.ndarray:
    """
    Remove stipple dots wherever the mask is dark (inside the letter).

    Parameters
    ----------
    stipple_img : np.ndarray
        Stippled image as 2D float array with values in [0, 1].
        Dark pixels (0.0) are stipple dots; light pixels (1.0) are background.
    mask_img : np.ndarray
        Mask image as 2D float array with values in [0, 1].
        Dark pixels (< threshold) define the masked-out region.
    threshold : float
        Pixels in mask_img below this value are treated as inside the mask.
        Default 0.5.

    Returns
    -------
    masked : np.ndarray
        2D float array with the same shape as the inputs. Stipple dots inside
        the mask region are replaced with white (1.0); all others are unchanged.
    """
    masked = stipple_img.copy()
    masked[mask_img < threshold] = 1.0
    return masked
