from PIL import Image
import numpy as np
import cv2

image = Image.open('uncompleted.png')
img = np.asarray(image)

count_white = 0
for i in range(len(img)):
    for j in range(len(img[i])):
        if str(img[i][j]) == '[255 255 255]':
            image.putpixel((j, i), (0, 0, 0))
            # count_white += 1
# print(count_white)
# image.save('white_completefortest.bmp')
image.show()