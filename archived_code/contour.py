import numpy as np
import cv2
from IPython import embed

im = cv2.imread('cropped_binary.png')
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(im_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
index  = 0;
for index in range(len(contours)):
	cnt = contours[index]
	area = cv2.contourArea(cnt)
	if area > 3000:
		#cv2.drawContours(im, [cnt], 0, (0, 0, 255), 3)
		print cnt
		start_x = cnt[0][0][1]
		end_x = cnt[2][0][1] + 1
		start_y = cnt[0][0][0]
		end_y = cnt[2][0][0] + 1
		im[start_x:end_x,start_y:end_y] = 255 - im[start_x:end_x,start_y:end_y]

cv2.imshow("contours", im)
cv2.imwrite("cropped_binary_contour.png", im)
cv2.waitKey()
