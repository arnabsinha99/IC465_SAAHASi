import cv2
import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('leaf1_marked.jpeg', 1)
img = cv2.imread('leaf9.jpg', 1)
# ret, th1 = cv2.threshold(img, 75, 255, cv2.THRESH_BINARY)
# ret,img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img = cv2.resize(img, (512, 512))
# img2 = cv2.resize(img2, (512, 512))

# color = ('b', 'g', 'r')
# for i, col in enumerate(color):
#     histr = cv2.calcHist([img], [i], None, [256], [0, 256])
#     plt.plot(histr, color=col)
#     plt.xlim([0, 256])
# plt.show()

# cv2.imshow('imga', th1)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)

# lower = np.array(lower, dtype="uint8")
# upper = np.array(upper, dtype="uint8")
# # find the colors within the specified boundaries and apply
# # the mask
# mask = cv2.inRange(image, lower, upper)
# output = cv2.bitwise_and(image, image, mask=mask)
# # show the images
# cv2.imshow("images", np.hstack([image, output]))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([10, 0, 10])
upper_green = np.array([50, 255, 100])


# low_green = np.array([10, 30, 60])
# high_green = np.array([120, 255, 255])


low_green = np.array([35, 0, 80])
high_green = np.array([80, 255, 255])
# mask of green (36,25,25) ~ (86, 255,255)
# mask = cv2.inRange(hsv, (36, 25, 25), (86, 255, 255))
mask = cv2.inRange(hsv, low_green, high_green)
# mask = cv2.inRange(hsv, (36, 25, 25), (70, 255, 255))
output = cv2.bitwise_and(img, img, mask=mask)
# slice the green
imask = mask > 0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

imask = mask == 0
spots = np.zeros_like(img, np.uint8)
spots[imask] = img[imask]

im = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

ret, th1 = cv2.threshold(im, 10, 255, cv2.THRESH_BINARY_INV)
# save
while(True):
    cv2.imshow("img", img)
    cv2.imshow("spot", spots)
    cv2.imshow("output", output)

    cv2.imshow("im", th1)

    # sp = np.zeros_like(img, np.uint8)
    # sp[255 for spot>0]

    # cv2.waitKey(0)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# closing all open windows
cv2.destroyAllWindows()
