import numpy as np
import cv2

img = cv2.imread('test-image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('test-image2.png', img)