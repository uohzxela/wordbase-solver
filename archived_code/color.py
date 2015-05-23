import numpy as np
import cv2

WHITE = 0
ORANGE = 1
BLUE = 2
BLACK = 3
img = cv2.imread('../images/cropped.png')
a = np.zeros(shape=(13,10))
for x in xrange(0, 832, 64):
	for y in xrange(0, 640, 64):
		px = img[x, y]
		print px
		blue = px[0]
		green = px[1]
		if blue == 0 and green==0:
			a[x/64,y/64] = BLACK
		elif blue <= 100:
			a[x/64,y/64] = ORANGE
		elif blue == 255:
			a[x/64,y/64] = WHITE
		else:
			a[x/64, y/64] = BLUE 

print a

