import numpy as np
import cv2
from math import sqrt

sigArray = [sqrt(2), sqrt(8), sqrt(32),sqrt(48),sqrt(64),sqrt(72) ]
def auto_canny(image, sigma):
	v = np.median(image)
	lower = int(max(0, (1.0 - sigma) * v)) # weak thres
	upper = int(min(255, (1.0 + sigma) * v)) # strong thres
	edged = cv2.Canny(image, lower, upper)
	return edged

img = cv2.imread('hus.png')

for i in sigArray:
    img = auto_canny(img, i)
    cv2.imshow("Canny with sigma = " + str(i), img)
    cv2.waitKey(4000)
    cv2.destroyAllWindows()