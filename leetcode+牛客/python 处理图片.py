from matplotlib.image import imread
from PIL.Image import open
import numpy as np
import cv2
from matplotlib import pyplot as plt
pic_path = r'C:\Users\Administrator\Pictures\1.png'
image1 = imread(pic_path)
image2 = open(pic_path)
# image2=cv2.imread(pic_path)[:,:,::-1];
array_2=np.array(image2)
print(image1 == image2)
print(image1.shape, '*****', array_2.shape)

plt.figure('TER')

plt.subplot(2, 1, 1)
plt.axis('off')
plt.imshow(image1)
plt.subplot(2, 1, 2)
plt.imshow(image2)

plt.show()
