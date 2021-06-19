from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
import cv2
import skimage.transform as trans


def train_generator(batch_size, path_to_train, image_folder, mask_folder, target_size, gen_args):
    image_datagen = ImageDataGenerator(**gen_args)
    mask_datagen = ImageDataGenerator(**gen_args)
    image_generator = image_datagen.flow_from_directory(
            path_to_train,
            target_size=target_size,
            classes=[image_folder],
            batch_size=batch_size)
    mask_generator = mask_datagen.flow_from_directory(
            path_to_train,
            target_size=target_size,
            classes=[mask_folder],
            batch_size=batch_size)
    train_generator = zip(image_generator, mask_generator)
    for (img, mask) in train_generator:
        yield (img, mask)


def testGenerator(test_path, num_image, target_size, flag_multi_class=False):
    for i in range(num_image):
        img = cv2.imread(os.path.join(test_path, "%d.jpg" % i))
        img = img / 255
        img = trans.resize(img, target_size)
        img = np.reshape(img, img.shape + (1,)) if (not flag_multi_class) else img
        img = np.reshape(img, (1,) + img.shape)
        yield img

