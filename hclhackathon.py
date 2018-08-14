import cv2
import numpy as np

img = cv2.imread('image.jpg') 
rsz_img = cv2.resize(img, None, fx=0.25, fy=0.25) 
gray = cv2.cvtColor(rsz_img, cv2.COLOR_BGR2GRAY)

retval, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255, type=cv2.THRESH_BINARY)

points = np.argwhere(thresh_gray==0)
points = np.fliplr(points) 
x, y, w, h = cv2.boundingRect(points)
x, y, w, h = x-10, y-10, w+20, h+20
crop = gray[y:y+h, x:x+w]

retval, thresh_crop = cv2.threshold(crop, thresh=200, maxval=255, type=cv2.THRESH_BINARY)

cv2.imshow("Cropped and thresholded image", thresh_crop) 
cv2.waitKey(0)
