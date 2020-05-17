import cv2
import numpy as np
from matplotlib import pyplot as plt


class DisparityMap:
    def draw(self, left_image, right_image, map_path):
        left = cv2.imread(left_image)
        left = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
        right = cv2.imread(right_image)
        right = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)

        stereo = cv2.StereoBM_create(
            numDisparities=64, blockSize=5
        )  # StereoSGBM_create
        disparity = stereo.compute(left, right)
        plt.imshow(disparity, 'gray')
        plt.savefig(map_path, dpi=199)
        plt.close()


class DisparityMap2:
    # https://rdmilligan.wordpress.com/2016/05/23/disparity-of-stereo-images-with-python-and-opencv/

    def draw(self, left_image, right_image, map_path):
        window_size = 5
        min_disp = 32
        num_disp = 112 - min_disp
        stereo = cv2.StereoSGBM_create(
            minDisparity=min_disp,
            numDisparities=num_disp,
            uniquenessRatio=10,
            speckleWindowSize=100,
            speckleRange=32,
            disp12MaxDiff=1,
            P1=8 * 3 * window_size ** 2,
            P2=32 * 3 * window_size ** 2,
        )

        # morphology settings
        kernel = np.ones((12, 12), np.uint8)
        image_left = cv2.imread(left_image)
        image_right = cv2.imread(right_image)
        disparity = stereo.compute(image_left, image_right)
        disparity = (disparity - min_disp) / num_disp
        threshold = cv2.threshold(disparity, 0.6, 1.0, cv2.THRESH_BINARY)[1]
        morphology = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
        plt.imshow(morphology, 'gray')
        plt.savefig(map_path.replace('.png', '_morphologyd.png'), dpi=199)
        plt.close()
        plt.imshow(threshold, 'gray')
        plt.savefig(map_path.replace('.png', '_threshold.png'), dpi=199)
        plt.close()
        plt.imshow(disparity, 'gray')
        plt.savefig(map_path.replace('.png', '_disparity.png'), dpi=199)
        plt.close()
