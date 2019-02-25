import cv2
from matplotlib import pyplot as plt
import numpy as np
"""
img = cv2.imread('family.JPG', 1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
plt.imshow(img, cmap = 'summer', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.plot([200,300,400],[100,200,300],'c',linewidth=2)
plt.show()
"""
 
cap = cv2.VideoCapture(0);
