import numpy as np
from PIL import Image, ImageOps
from numpy.typing import NDArray
from typing import Tuple, Union

THRESHOLD = 100
FINAL_SIZE = 20
MNIST_SIZE = 28


class Utils:
    """
    Class for image preprocessing (before recognition)
    """

    @classmethod
    def get_formatted_image(cls, pil_im: Image, as_ndarray=True) -> Union[Image.Image, NDArray]:
        """
        Converts an image of the number into NumPy array
        """
        pil_im = cls._get_cropped_image(cls._get_gscale_image(pil_im))
        pil_im = pil_im.resize((FINAL_SIZE, FINAL_SIZE), resample=1)
        pil_im = cls._paste_on_black_square(pil_im)
        return np.array(pil_im) if as_ndarray else pil_im

    @staticmethod
    def _get_gscale_image(img: Image, inverse=True) -> Image:
        """
        Converts image into a black-white one
        """
        converted_image = img.convert('1')
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
    def _get_boundaries(np_img: NDArray, inverted_image=True) -> Tuple:
        """
        Gets boundaries of the image
        """
        x = {k: v for k, v in enumerate(np_img.sum(axis=1) / np_img.shape[1])}
        y = {k: v for k, v in enumerate(np_img.sum(axis=0) / np_img.shape[0])}

        x = list(filter(lambda z: (z[1] > 0) if inverted_image else (z[1] < 255), x.items()))
        y = list(filter(lambda z: (z[1] > 0) if inverted_image else (z[1] < 255), y.items()))

        return min(x)[0], min(y)[0], max(x)[0], max(y)[0]

    @staticmethod
    def _paste_on_black_square(img: Image) -> Image:
        """
        Pastes 20x20 image on the black square with size 28x28
        """
        modified_image = Image.fromarray(np.zeros((MNIST_SIZE, MNIST_SIZE)))
        start_position = int((MNIST_SIZE - FINAL_SIZE) / 2)
        modified_image.paste(img, (start_position, start_position))
        return modified_image

