# ------------------------------------------------------
import cv2
import numpy as np

img = cv2.imread("img5.jpeg", 0)
cv2.imwrite("img5_gray.jpeg", img)

# img = cv.medianBlur(img, 5)
ret, th1 = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

cv2.imwrite("img5_gray_thrs.jpeg", th1)
