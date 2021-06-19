import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2

image = Image.open('decisiontest35.png').save('des.bmp') # img with notes save as bmp
image = Image.open('des.bmp')
img = np.asarray(image)
pix_coords = []
n, h = 0, 0
for i in range(len(img)):
    for j in range(len(img[i])):
        if str(img[i][j]) == '[255   0   0]':
            # if n == 4:
            #     break
            # else:
                # i[j] = np.array([.0, .255, .0])
            pix_coords.append((j, i)) # j, i coords in pix_coords list
            n += 1
                # print(i[j])
print(n, h)
print(pix_coords)
# [(298, 211), (307, 211), (298, 213), (307, 213),
# (325, 254), (315, 255), (343, 260), (327, 262), (345, 266), (319, 269)] (n, h)
# print(image.size)
    # r, g, b = image.getpixel((319, 269))
    # image.putpixel((319, 269), (0, 255, 0))
    # image.show()
# print(r, g, b)
y = 0
a = np.array(pix_coords)
# print(a)
# cv2.drawContours(img, [a], 0, (255,255,255), 2)
# cv2.imshow('df', cv2.drawContours(img, [a], 0, (255,255,255), 2))
# cv2.line(img, (315, 255), (325, 254), [0, 255, 0], 2)
# cv2.line(img, (325, 254), (327, 262), [0, 255, 0], 2)
# cv2.line(img, (327, 262), (343, 260), [0, 255, 0], 2)
# cv2.line(img, (343, 260), (345, 266), [0, 255, 0], 2)
# cv2.line(img, (319, 269), (345, 266), [0, 255, 0], 2)
# cv2.line(img, (315, 255), (319, 269), [0, 255, 0], 2)
contours = np.array([(544, 195), (563, 196), (562, 200), (544, 199)]) # First build. Pairs of coords from pix_coords
contours1 = np.array([(561, 229), (567, 230), (562, 240), (556, 239)]) # Second build. Pairs of coords from pix_coords
# contours2 = np.array([(555, 200), (553, 199), (549, 201), (557, 200), (560, 201), (559, 201), (562, 202), (555, 206), (552, 203), (551, 203)])
# contours3 = np.array([(490, 232), (466, 234), (454, 236), (455, 238)])
cv2.fillPoly(img, pts=[contours, contours1], color=(0,0,255)) # Fill space between notes with color
cv2.imshow('fds', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
cv2.imwrite('white_test35.bmp', img) # Save no norm img