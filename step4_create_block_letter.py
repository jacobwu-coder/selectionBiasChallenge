"""
Step 4: Create a block letter image matching the input image dimensions.
Uses PIL to render a bold letter centered and scaled to fill the image.
"""

import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def create_block_letter_s(
    height: int,
    width: int,
    letter: str = "S",
    font_size_ratio: float = 0.9,
) -> np.ndarray:
    """
    Generate a block letter centered and scaled to fit within image dimensions.

    Parameters
    ----------
    height : int
        Height of the output image in pixels.
    width : int
        Width of the output image in pixels.
    letter : str
        The letter to render. Default "S".
    font_size_ratio : float
        Fraction of the smaller image dimension to use as the font size.
        Default 0.9.

    Returns
    -------
    letter_array : np.ndarray
        2D float array (height × width) with values in [0, 1].
        Letter pixels are 0.0 (black); background pixels are 1.0 (white).
    """
    # White background canvas
    img = Image.new("L", (width, height), color=255)
    draw = ImageDraw.Draw(img)

    font_size = int(min(height, width) * font_size_ratio)

    # Try bold system fonts in order; fall back to PIL default if none found
    font_candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]

    font = None
    for path in font_candidates:
        if os.path.exists(path):
            try:
                font = ImageFont.truetype(path, font_size)
                break
            except Exception:
                continue

    if font is None:
        font = ImageFont.load_default()

    # Measure rendered letter and center it on the canvas
    bbox = draw.textbbox((0, 0), letter, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (width - text_w) // 2 - bbox[0]
    y = (height - text_h) // 2 - bbox[1]

    draw.text((x, y), letter, fill=0, font=font)

    return np.array(img, dtype=np.float32) / 255.0
