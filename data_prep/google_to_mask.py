from PIL import Image
import numpy as np
import cv2

image = Image.open('../new_data/masks/1w.bmp') # with buildings
img = np.asarray(image)

count_white = 0
margin = 0 # 255 ~255 255 0~
for i in range(len(img)):
    for j in range(len(img[i])):
        if sum(img[i][j]) != 255 * 3 - margin:
            image.putpixel((j, i), (0, 0, 0))
            # count_white += 1
# print(count_white)
image.save('FINISH_MASK1.jpg')
image.show()

g = 0
for i in range(len(img)):
    for j in range(len(img[i])):
        if str(img[i][j]) == '[255  255  255]':
            g += 1
print(g)