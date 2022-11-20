import numpy as np
from PIL import Image, ImageOps
from numpy.typing import NDArray
from typing import Tuple, Union

THRESHOLD = 100
FINAL_SIZE = 28


class Utils:

    @classmethod
    def get_formatted_image(cls, pil_im: Image, as_ndarray=True) -> Union[Image.Image, NDArray]:
        """
        Converts an image of the number into NumPy array
        """
        pil_im = cls._get_cropped_image(cls._get_bw_image(pil_im))
        pil_im = pil_im.resize((FINAL_SIZE, FINAL_SIZE), resample=1)
        pil_im = cls._get_bw_image(pil_im, inverse=False)
        return np.array(pil_im) if as_ndarray else pil_im

    @staticmethod
    def _get_bw_image(img: Image, inverse=True) -> Image:
        """
        Converts image into a black-white one
        """
        converted_image = img.convert('L').point(lambda x: 255 if x > THRESHOLD else 0, mode='1')
        return ImageOps.invert(converted_image) if inverse else converted_image

    @classmethod
    def _get_cropped_image(cls, img: Image) -> Image:
        """
        Crops the image (converts the image into a squared one)
        """
        img_np = np.array(img)
        boundaries = cls._get_boundaries(img_np)
        img_np = img_np[boundaries[0]: boundaries[2], boundaries[1]: boundaries[3]]
        return Image.fromarray(img_np)

    @staticmethod
    def _get_boundaries(np_img: NDArray) -> Tuple:
        """
        Gets boundaries of the image
        """
        x = {k: v for k, v in enumerate(np_img.sum(axis=1) / np_img.shape[1])}
        y = {k: v for k, v in enumerate(np_img.sum(axis=0) / np_img.shape[0])}

        x = list(filter(lambda z: z[1] > 0, x.items()))
        y = list(filter(lambda z: z[1] > 0, y.items()))

        return min(x)[0], min(y)[0], max(x)[0], max(y)[0]

