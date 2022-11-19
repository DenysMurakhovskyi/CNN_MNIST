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
        self.assertEqual((200, 160), np.array(bw_image).shape)

    def test_get_boundaries(self):
        actual = Utils._get_boundaries(np.array(Utils._get_bw_image(self.img)))
        self.assertEqual((25, 30, 174, 123), actual)

    def test_full_process(self):
        img_np = Utils.get_formatted_image_as_ndarray(self.img)
        Image.fromarray(img_np).show()

