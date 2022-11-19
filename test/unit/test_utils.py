from unittest import TestCase

from application.utils import Utils
import pathlib
from PIL import Image
import numpy as np
from numpy.testing import assert_array_equal


class UtilsTest(TestCase):

    def setUp(self) -> None:
        path = pathlib.Path(__file__).parents[1].resolve() / 'test_files/image_1.png'
        self.img = Image.open(path)

    def test_bw_image(self):
        bw_image = Utils._get_bw_image(self.img)
        assert_array_equal(np.array([0, 255]), np.unique(np.array(bw_image)))

