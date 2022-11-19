import os

import numpy as np
from PIL import Image, ImageOps
from numpy.typing import ArrayLike

THRESHOLD = 100


class Utils:

    @staticmethod
    def get_ndarray_from_image(pil_im: Image) -> ArrayLike:
        grayscale = ImageOps.grayscale(pil_im).resize((20, 20), resample=1)  # image grayscale
        np_img = np.array(grayscale)  # image to a NumPy array
        np_img = np.vectorize(lambda x: 0 if x < THRESHOLD else 255)(np_img)  # gets black/white image (binary)

        # shows image for debug purpose only
        if os.environ.get('DEBUG', '0') == '1':
            img = Image.fromarray(np_img)
            img.show()

        # returns image as a numpy array
        return np_img