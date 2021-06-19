from PIL import Image
import numpy as np
import cv2

image = Image.open('start_with_no_norm35.png') # with buildings
img = np.asarray(image)
count_white = 0
margin = 250 # 255 ~255 255 0~
for i in range(len(img)):
    for j in range(len(img[i])):
        if (255*3) - (int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2])) <= margin:
            image.putpixel((j, i), (0, 0, 0))
            # count_white += 1
# print(count_white)
image.save('START35.png')
image.show()

# im_gray = cv2.imread(r'C:\projects\kai_prj\start_with_no_norm.png')
# _, mask = cv2.threshold(im_gray, thresh=180, maxval=255, type=cv2.THRESH_BINARY)
# im_thresh_gray = cv2.bitwise_and(im_gray, mask)
# cv2.imshow('dcds', im_thresh_gray)
# cv2.waitKey()
# cv2.destroyAllWindows()
# # cv2.imwrite('complete.bmp', im_thresh_gray)