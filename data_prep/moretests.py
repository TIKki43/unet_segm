import numpy as np
import matplotlib.pyplot as plt
from new_id import b
from PIL import Image

n = 0
# X = np.random.normal(0, 1, n)
# Y = np.random.normal(0, 1, n)
# T = np.arctan2(Y, X)

# plt.axes([0.05, 0.05, 0.9, 0.9])
# plt.scatter(X, Y, s=75, c=T, alpha=.5)
img = Image.open(f'C:\projects\kai_prj\dataset\sentinelhub/decisiontest35.jpg') # sentinelhub img
# print(img)
img = plt.imshow(img, extent=[47.410604,47.426901,55.609696,55.614289]) # small to large coords of img in new_id (47.229596, 47.245893, 56.206010, 56.210534)
plt.savefig('start_with_no_norm35.png')
for i in b:
    plt.plot(i[0], i[1], ',', color='#FF0000')
    # print(i)
    n += 1
print(n)
# img.get_image()
plt.savefig('decisiontest35.png')
# plt.imshow(extent=[5, 10, 5, 10])
# plt.imsave('C:\projects\kai_prj\decisiontest.jpg', img)
plt.show()
# for i in np.asarray(img):
#     for j in i:
#         print(j)
#         break
#     break
np.asarray(img)