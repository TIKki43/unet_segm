from data_work import *
from model import *

data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')

tr = train_generator(1, '/home/timur/Documents/Projects/unet_segm/New_new_data/train', 'cl_img', 'masks', (256, 256), data_gen_args)

unet = unet()
unet_checkpoint = ModelCheckpoint('unet.hdf5', monitor='loss')
unet.fit_generator(tr, steps_per_epoch=300, epochs=1, callbacks=[unet_checkpoint])
