from PIL import Image
import numpy as np
import cv2

image = Image.open('white_test34.bmp') # with buildings
img = np.asarray(image)

count_white = 0
margin = 450 # 255 ~255 255 0~
for i in range(len(img)):
    for j in range(len(img[i])):
        if (255*3) - (int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2])) <= margin:
            image.putpixel((j, i), (0, 0, 0))
            # count_white += 1
# print(count_white)
image.save('red_completefortest6.bmp')
image.show()
im_gray = cv2.imread(r'C:\projects\kai_prj\red_completefortest6.bmp')
_, mask = cv2.threshold(im_gray, thresh=180, maxval=255, type=cv2.THRESH_BINARY)
im_thresh_gray = cv2.bitwise_and(im_gray, mask)
# cv2.imshow('dcds', im_thresh_gray)
# cv2.waitKey(10000)
# cv2.destroyAllWindows()
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# ret, threshold_image = cv2.threshold(im, 127, 255, 0)
cv2.imwrite('FINISH34.bmp', im_thresh_gray)



cv2.imwrite('completefortest1_white.bmp', im_thresh_gray)



image = Image.open('white_testfortest.bmp') # with buildings
img = np.asarray(image)

count_white = 0
margin = 155 # 255 ~255 255 0~
for i in range(len(img)):
    for j in range(len(img[i])):
        if (255*3) - (int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2])) <= margin:
            image.putpixel((j, i), (0, 0, 0))
            # count_white += 1
# print(count_white)
image.save('white_completefortest1.bmp')
image.show()
im_gray = cv2.imread(r'C:\projects\kai_prj\white_completefortest1.bmp')
_, mask = cv2.threshold(im_gray, thresh=180, maxval=255, type=cv2.THRESH_BINARY)
im_thresh_gray = cv2.bitwise_and(im_gray, mask)
cv2.imshow('dcds', im_thresh_gray)
cv2.waitKey(10000)
cv2.destroyAllWindows()
# cv2.imwrite('completefortest1_white.bmp', im_thresh_gray)