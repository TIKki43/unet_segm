from data_work import *
# from main import *
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from PIL import Image

model = load_model('unet.h5')

path_to_test = '/home/timur/Documents/Projects/unet_segm/New_new_data/test'

# test = testGenerator(path_to_test, 11, (-1, 256, 256, 1))
img = Image.open('New_new_data/test/5.jpg')
img = np.asarray(img)
img = img / 255
img = np.resize(img, (256, 256))
img = np.reshape(img, (-1, 256, 256, 1))
pred = model.predict(img) * 255
print(pred)
# img = Image.fromarray(pred)
# img.save('0_pred.png')
# img.show()
plt.imshow(np.reshape(pred, (256, 256, 1)))
plt.show()