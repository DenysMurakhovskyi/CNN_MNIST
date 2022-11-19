import numpy as np
from PIL import Image, ImageOps
from numpy.typing import NDArray
from typing import Tuple

THRESHOLD = 100


class Utils:

    @classmethod
    def get_formatted_image_as_ndarray(cls, pil_im: Image) -> NDArray:
        pil_im = cls._get_cropped_image(cls._get_bw_image(pil_im))
        pil_im = pil_im.resize((28, 28), resample=1)
        return np.array(cls._get_bw_image(pil_im))

    @staticmethod
    def _get_bw_image(img: Image) -> Image:
        grayscale = ImageOps.grayscale(img)
        np_img = np.array(grayscale)
        np_img = np.vectorize(lambda x: 0 if x < THRESHOLD else 255)(np_img)
        return Image.fromarray(np_img)

    @classmethod
    def _get_cropped_image(cls, img: Image) -> Image:
        img_np = np.array(img)
        boundaries = cls._get_boundaries(img_np)
        img_np = img_np[boundaries[0]: boundaries[2], boundaries[1]: boundaries[3]]
        return Image.fromarray(img_np)

    @staticmethod
    def _get_boundaries(np_img: NDArray) -> Tuple:
        x = {k: v for k, v in enumerate(np_img.sum(axis=1) / np_img.shape[1])}
        y = {k: v for k, v in enumerate(np_img.sum(axis=0) / np_img.shape[0])}

        x = list(filter(lambda z: z[1] < 255, x.items()))
        y = list(filter(lambda z: z[1] < 255, y.items()))

        return min(x)[0], min(y)[0], max(x)[0], max(y)[0]
