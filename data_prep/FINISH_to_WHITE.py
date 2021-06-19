from PIL import Image
import numpy as np
import cv2
a = 20
for i in range(14):
    a += 1
    image = Image.open(f'FINISH{a}.bmp')
    img = np.asarray(image)
    for i in range(len(img)):
        for j in range(len(img[i])):
            if str(img[i][j]) == '[255   0   0]':
                image.putpixel((j, i), (255,255,255))
                image.save(f'FINISH_WHITE{a}.bmp')
            else:
                image.putpixel((j, i), (0, 0, 0))
                image.save(f'FINISH_WHITE{a}.bmp')