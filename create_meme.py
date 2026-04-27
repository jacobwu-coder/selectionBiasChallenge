"""
Final Step: Assemble all four panels into a statistics meme and save as PNG.
"""

import numpy as np
import matplotlib.pyplot as plt


def create_statistics_meme(
    original_img: np.ndarray,
    stipple_img: np.ndarray,
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str,
    dpi: int = 150,
    background_color: str = "white",
) -> None:
    """
    Assemble four image panels into a professional statistics meme and save.

    Parameters
    ----------
    original_img : np.ndarray
        Grayscale original image — the "Reality" panel.
    stipple_img : np.ndarray
        Stippled version of the image — the "Your Model" panel.
    block_letter_img : np.ndarray
        Block letter S image — the "Selection Bias" panel.
    masked_stipple_img : np.ndarray
        Stippled image with letter mask applied — the "Estimate" panel.
    output_path : str
        File path to save the output PNG.
    dpi : int
        Resolution in dots per inch. Default 150.
    background_color : str
        Figure background color. Default "white".
    """
    panel_labels = ["Reality", "Your Model", "Selection Bias", "Estimate"]
    images = [original_img, stipple_img, block_letter_img, masked_stipple_img]

    fig, axes = plt.subplots(1, 4, figsize=(16, 5), facecolor=background_color)
    fig.subplots_adjust(wspace=0.04, left=0.01, right=0.99, top=0.82, bottom=0.02)

    for ax, img, label in zip(axes, images, panel_labels):
        ax.imshow(img, cmap="gray", vmin=0, vmax=1)
        ax.axis("off")
        ax.set_title(label, fontsize=16, fontweight="bold", pad=8, color="black")

    fig.suptitle(
        "Selection Bias: Systematic Missing Data Distorts Your Estimate",
        fontsize=13,
        fontweight="bold",
        y=0.97,
        color="#333333",
    )

    plt.savefig(
        output_path,
        dpi=dpi,
        bbox_inches="tight",
        facecolor=background_color,
        edgecolor="none",
    )
    plt.close(fig)
    print(f"Meme saved to {output_path}")
