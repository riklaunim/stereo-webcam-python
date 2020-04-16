import os

from libraries import frame_splitter

FRAMES_DIR = './example_frames'
SPLIT_FRAMES_DIR = './splitted'

frames = os.listdir(FRAMES_DIR)
for frame in frames:
    path = os.path.join(FRAMES_DIR, frame)
    print(path)
    splitter = frame_splitter.StereoFrameSplitter(path)
    left, right = splitter.get_stereo_frames()
    left_file = os.path.join(SPLIT_FRAMES_DIR, f'l_{frame}')
    right_file = os.path.join(SPLIT_FRAMES_DIR, f'r_{frame}')
    left.save(left_file)
    right.save(right_file)
