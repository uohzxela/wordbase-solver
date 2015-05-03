from PIL import Image
import cv2
import numpy as np
import pytesseract
import sys
WHITE = 0
ORANGE = 1
BLUE = 2
BLACK = 3
# image_file_path is supplied from command line args
# resize to 640 x 1136 before doing anything
def resize_and_crop(image_file_path):
	try: 
		pil_image = Image.open(image_file_path)
	except IOError:
		sys.stderr.write('ERROR: Could not open file "%s"\n' % image_file_path)
		exit(1)
	size = (640, 1136)
	pil_image.thumbnail(size, Image.ANTIALIAS)
	pil_image = pil_image.crop((0,304,640,1136))
	return pil_image

def pil_to_opencv(pil_image):
	opencv_image = np.array(pil_image) 
	opencv_image = opencv_image[:, :, ::-1].copy()
	return opencv_image
	
# perform simple thresholding (BINARY_INV)
def simple_threshold(opencv_image):
	gray_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
	(T, thresh) = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY_INV)
	return thresh

# find blobs of white and invert it to black
def find_contours_and_invert(opencv_image):
	im = cv2.cvtColor(opencv_image, cv2.COLOR_GRAY2BGR)
	im_binary = opencv_image
	contours, hierarchy = cv2.findContours(im_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	index  = 0;
	for index in range(len(contours)):
		cnt = contours[index]
		area = cv2.contourArea(cnt)
		if area > 3000:
			# cv2.drawContours(im, [cnt], 0, (0, 0, 255), 3)
			# print cnt
			start_x = cnt[0][0][1]
			end_x = cnt[2][0][1] + 1
			start_y = cnt[0][0][0]
			end_y = cnt[2][0][0] + 1
			im[start_x:end_x,start_y:end_y] = 255 - im[start_x:end_x,start_y:end_y]
	return im

def opencv_to_pil(opencv_im):
	opencv_im = cv2.cvtColor(opencv_im,cv2.COLOR_BGR2RGB)
	pil_im = Image.fromarray(opencv_im)
	return pil_im

def generate_color_map(opencv_im):
	img = opencv_im
	a = np.zeros(shape=(13,10))
	for x in xrange(0, 832, 64):
		for y in xrange(0, 640, 64):
			px = img[x, y]
			# print px
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
	# print a
	return a


def get_gameboard(img):
  	image_file_path = img
	pil_image = resize_and_crop(image_file_path)
	opencv_image = pil_to_opencv(pil_image)
	color_map = generate_color_map(opencv_image)
	thresh = simple_threshold(opencv_image)
	opencv_image = find_contours_and_invert(thresh)
	pil_image = opencv_to_pil(opencv_image)
	gameboard = pytesseract.image_to_string(pil_image, config="-psm 6")
	return gameboard, color_map

def get_matrix(img):
	gameboard, color_map = get_gameboard(img)
	characters = [char for char in gameboard if char.isalnum()]
	matrix = [[characters[x*10 + y] for y in range(0,10)] for x in range(0,13)]
	return matrix, color_map

def main():
	if len(sys.argv) == 2:
		print get_gameboard(sys.argv[1])
	else:
		sys.stderr.write('Usage: python extract_gameboard.py image_file_path\n')
		exit(2)

if __name__ == '__main__':
    main()
