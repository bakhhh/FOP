#
# prettyface.py
#
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from scipy import misc

face = misc.face(gray=True)
plt.imshow(face)
plt.show()
plt.imshow(face, cmap=plt.cm.gray)
plt.show()

shifted_face = ndimage.shift(face, (50,50))
plt.imshow(shifted_face)
plt.show()

cropped_face = face[100:-100,100:-100]
plt.imshow(cropped_face)
plt.show()

print(np.shape(face))
plt.imshow(face)
pixel_face = face[::10,::10]
print(np.shape(pixel_face))
plt.imshow(pixel_face)
plt.show()
pixel_face2 = face[::50,::50]
print(np.shape(pixel_face2))
plt.imshow(pixel_face2)
plt.show()
