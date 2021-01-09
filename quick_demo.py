import os
import sys
import skimage.io
import matplotlib.pyplot as plt

from mrcnn.config import Config
from mrcnn import model as modellib
from mrcnn import visualize

ROOT_DIR = os.getcwd()
sys.path.append(ROOT_DIR)

MODEL_DIR = os.path.join(ROOT_DIR, "logs")
MODEL_PATH = os.path.join(ROOT_DIR, "logs/models/mask_rcnn_shapes_0040.h5")

class ShapesConfig(Config):
    NAME = "shapes"
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 1 + 1  # background + text

    IMAGE_MIN_DIM = 256
    IMAGE_MAX_DIM = 640

    RPN_ANCHOR_SCALES = (8 * 8, 16 * 16, 32 * 16, 64 * 16, 128 * 16)
    TRAIN_ROIS_PER_IMAGE = 32
    STEPS_PER_EPOCH = 100
    VALIDATION_STEPS = 5


class TextConfig(ShapesConfig):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


config = TextConfig()
config.display()
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
model.load_weights(MODEL_PATH, by_name=True)

class_names = ['BG', 'text']
file_name = os.path.join(ROOT_DIR, "pictures/4.jpg")
image = skimage.io.imread(file_name)

results = model.detect([image], verbose=1)
r = results[0]
visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'],
                            class_names, r['scores'])



