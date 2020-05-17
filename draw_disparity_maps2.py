import os

from libraries import disparity2

FRAMES_DIR = './example_frames'
SPLIT_FRAMES_DIR = './splitted'
DISPARITY_MAPS_DIR = './disparity_maps2'

frames = os.listdir(FRAMES_DIR)
for frame in frames:
    print(frame)
    left_file = os.path.join(SPLIT_FRAMES_DIR, f'l_{frame}')
    right_file = os.path.join(SPLIT_FRAMES_DIR, f'r_{frame}')

    filename = frame.split('.')[0]
    filename = f'{filename}.png'
    map_path = os.path.join(DISPARITY_MAPS_DIR, filename)
    disparity2.draw(left_file, right_file, map_path)
