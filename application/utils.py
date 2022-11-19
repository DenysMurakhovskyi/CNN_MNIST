import os

import numpy as np
from PIL import Image, ImageOps
from numpy.typing import ArrayLike

THRESHOLD = 100


class Utils:

    @classmethod
    def get_formatted_image_as_ndarray(cls, pil_im: Image) -> ArrayLike:
        pil_im = cls._get_bw_image(pil_im)
        pil_im = cls._get_centered_image(pil_im)
        pil_im = cls._get_rescaled_image(pil_im)
        return np.array(pil_im)

    @staticmethod
    def _get_bw_image(img: Image) -> Image:
        grayscale = ImageOps.grayscale(img)
        np_img = np.array(grayscale)  # image to a NumPy array
        np_img = np.vectorize(lambda x: 0 if x < THRESHOLD else 255)(np_img)
        return Image.fromarray(np_img)

    @staticmethod
    def _get_rescaled_image(img: Image):
        pass

    @staticmethod
    def _get_centered_image(img: Image):
        (X, Y) = img.size
        img_np = np.array(img)

        m = np.sum(img_np, -1) < 255 * 3
        m = m / np.sum(np.sum(m))

        dx, dy = np.sum(m, 0), np.sum(m, 1)
        cx, cy = np.sum(dx * np.arange(X)), np.sum(dy * np.arange(Y))
        pass

    @staticmethod
    def _to_numpy_array(img: Image) -> ArrayLike:
        pass
