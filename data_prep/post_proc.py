from PIL import Image, ImageEnhance
import numpy as np
from scipy.misc import *

for i in range(11):
    img = Image.open(f'{i}_predict.png')
    enhancer = ImageEnhance.Contrast(img)

    factor = 10
    im_output = enhancer.enhance(factor)
    im_output.save(f'more-contrast-image{i}.png')
