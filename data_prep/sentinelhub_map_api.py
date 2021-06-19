from sentinelhub import SHConfig
import datetime
import numpy as np
import matplotlib.pyplot as plt
from sentinelhub import WmsRequest, WcsRequest, MimeType, CRS, BBox
from PIL import Image
import PIL
# from osm_api import common_shape

INSTANCE_ID = 'ef568278-7345-4b1e-b9bd-271ed318b353'

if INSTANCE_ID:
    config = SHConfig()
    config.instance_id = INSTANCE_ID
else:
    config = None


def plot_image(image, factor=1):
    fig = plt.subplots(nrows=1, ncols=1, figsize=(15, 7))

    if np.issubdtype(image.dtype, np.floating):
        return np.minimum(image * factor, 1)
    else:
        return image


data_coords = [49.238384,55.723437,49.258833,55.728910]#[49.086174,55.808933,49.106644,55.814648] # lng/lat
# print(data_coords[0] - data_coords[2], data_coords[1] - data_coords[3])

data_coords = BBox(bbox=data_coords, crs=CRS.WGS84)
# width, height = common_shape[1], common_shape[0]

true_color_request = WmsRequest(
    layer='TRUE-COLOR-S2L2A',  # first_layer
    bbox=data_coords,
    time='2020-10-13',   # odd
    width=1792,
    height=768,
    config=config
)

# print(common_shape[0], common_shape[1])
true_color_img = true_color_request.get_data()
plt.imshow(plot_image(true_color_img[-1]))
plt.show()
# plt.imsave('/home/timur/Projects/kai_prj/dataset/sentinelhub/TEST1.jpg', plot_image(true_color_img[-1]))
