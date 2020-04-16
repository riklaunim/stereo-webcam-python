import functools

from PIL import Image


class StereoFrameSplitter:
    BORDER = 1

    def __init__(self, image_file):
        self.image_file = image_file

    def get_stereo_frames(self):
        left, right = self._get_subframes_regions()
        left_image = self.image.crop(left)
        right_image = self.image.crop(right)
        return left_image, right_image

    def _get_subframes_regions(self):
        width, height = self.image.size
        half_width = int(width / 2)
        return [(0, 0, half_width - self.BORDER, height), (half_width + self.BORDER, 0, width, height)]

    @functools.cached_property
    def image(self):
        return Image.open(self.image_file)
