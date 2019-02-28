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
"""
cap = cv2.VideoCapture("test.mp4")
while(True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release
cv2.destroyAllWindows
"""
img = cv2.imread('girl.jpeg', cv2.IMREAD_COLOR)
img[55, 55] = [255, 255, 255]
px = img[55, 55]
print(px)
px = img[100:150, 100:150]
print(px)
