import cv2
import numpy as np
import pandas as pd

#KEY STROKES OF RIGHT HAND AS CSV FILE
right_key_order = pd.read_csv("Right_Hand_Keys.csv")

right_np_arr    = np.array(right_key_order)

#KEY STROKES OF LEFT HAND AS CSV FILE
left_key_order = pd.read_csv("Left_Hand_Keys.csv")

left_np_arr    = np.array(left_key_order)

#Keyboard Picture 
base_img = cv2.imread("keyboard_highres.png")

width  = int(base_img.shape[1])
height = int(base_img.shape[0])

frameSize = (width, height)

fourcc  = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output_video.avi',fourcc, 5.1, frameSize)

key_pic = []
#Pictures of Keys
#OCTAVE 1
key_pic.append(cv2.imread("key_highres.png"))
key_pic.append(cv2.imread("3D.png"))
key_pic.append(cv2.imread("3E.png"))
key_pic.append(cv2.imread("3F.png"))
key_pic.append(cv2.imread("3G.png"))
key_pic.append(cv2.imread("3A.png"))
key_pic.append(cv2.imread("3B.png"))
#OCTAVE 2
key_pic.append(cv2.imread("2C.png"))
key_pic.append(cv2.imread("2D.png"))
key_pic.append(cv2.imread("2E.png"))
key_pic.append(cv2.imread("2F.png"))
key_pic.append(cv2.imread("2G.png"))
key_pic.append(cv2.imread("2A.png"))
key_pic.append(cv2.imread("2B.png"))
#OCTAVE 3
key_pic.append(cv2.imread("C.png"))
key_pic.append(cv2.imread("D.png"))
key_pic.append(cv2.imread("E.png"))
key_pic.append(cv2.imread("F.png"))
key_pic.append(cv2.imread("G.png"))
key_pic.append(cv2.imread("A.png"))
key_pic.append(cv2.imread("B.png"))
#OCTAVE 4
key_pic.append(cv2.imread("C1.png"))
key_pic.append(cv2.imread("D1.png"))
key_pic.append(cv2.imread("E1.png"))
key_pic.append(cv2.imread("F1.png"))
key_pic.append(cv2.imread("G1.png"))
key_pic.append(cv2.imread("A1.png"))
key_pic.append(cv2.imread("B1.png"))
#OCTAVE 5
key_pic.append(cv2.imread("C2.png"))
key_pic.append(cv2.imread("D2.png"))
key_pic.append(cv2.imread("E2.png"))
key_pic.append(cv2.imread("F2.png"))
key_pic.append(cv2.imread("G2.png"))
key_pic.append(cv2.imread("A2.png"))
key_pic.append(cv2.imread("B2.png"))
#OCTAVE 6
key_pic.append(cv2.imread("C3.png"))

#FINDING THE THRESHOLD IMAGES OF EACH KEYS
thresh = []

row, column = right_np_arr.shape

base_img2 = base_img.copy()

for i in range(len(key_pic)):
	
	gray = cv2.cvtColor(key_pic[i], cv2.COLOR_BGR2GRAY)

	ret, dummy_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

	thresh.append(dummy_thresh)

img_comp = np.zeros((height,width,3),np.uint8)

base_img = cv2.addWeighted(base_img, 0.5, img_comp, 0.5, 0.0)

for i in range(row):
	dummy = base_img.copy()
	for j in range(column):
		if(right_np_arr[i,j]==1):
			dummy[thresh[j]==255] = [180,105,255]
		if(left_np_arr[i,j]==1):
			dummy[thresh[j]==255] = [250,191,0]
	dummy = cv2.addWeighted(base_img, 0.3, dummy, 0.7, 0.0)
	out.write(dummy)

out.release()