#!/usr/bin/env python3
import pathlib

import cv2
import numpy as np
import PIL.Image
import sklearn.datasets
import tensorflow as tf


def _main():
    output_dir = pathlib.Path("images")
    output_dir.mkdir(parents=True, exist_ok=True)

    original_image = sklearn.datasets.load_sample_image("china.jpg")
    save_image(output_dir / "original.jpg", original_image)

    for mode in ["reduction", "magnification", "mixed"]:
        if mode == "reduction":
            img = original_image
        elif mode == "magnification":
            x, y = 300, 300
            img = original_image[y : y + 32, x : x + 32]
        else:
            x, y = 0, 300
            img = original_image[y : y + 32, x : x + 512]

        save_image(
            output_dir / f"{mode}_cv2_area.jpg",
            cv2.resize(img, (128, 128), interpolation=cv2.INTER_AREA),
        )
        save_image(
            output_dir / f"{mode}_cv2_lanc.jpg",
            cv2.resize(img, (128, 128), interpolation=cv2.INTER_LANCZOS4),
        )
        save_image(
            output_dir / f"{mode}_pil_near.jpg",
            np.asarray(PIL.Image.fromarray(img).resize((128, 128), PIL.Image.NEAREST)),
        )
        save_image(
            output_dir / f"{mode}_pil_lanc.jpg",
            np.asarray(PIL.Image.fromarray(img).resize((128, 128), PIL.Image.LANCZOS)),
        )
        save_image(
            output_dir / f"{mode}_tf_area.jpg",
            tf.image.resize(img, (128, 128), "area").numpy().astype(np.uint8),
        )
        save_image(
            output_dir / f"{mode}_tf_lanc.jpg",
            tf.image.resize(img, (128, 128), "lanczos5", antialias=True)
            .numpy()
            .astype(np.uint8),
        )


def save_image(path, img):
    PIL.Image.fromarray(img).save(path)


if __name__ == "__main__":
    _main()
