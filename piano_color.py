import cv2
import numpy as np
import pandas as pd

#KEY STROKES OF RIGHT HAND AS CSV FILE
right_key_order = pd.read_csv("Melody_CSV/Right_Hand_Keys.csv")

right_np_arr    = np.array(right_key_order)

#KEY STROKES OF LEFT HAND AS CSV FILE
left_key_order = pd.read_csv("Melody_CSV/Left_Hand_Keys.csv")

left_np_arr    = np.array(left_key_order)

#Keyboard Picture 
base_img = cv2.imread("Photos/keyboard_highres.png")

width  = int(base_img.shape[1])
height = int(base_img.shape[0])

frameSize = (width, height)

fourcc  = cv2.VideoWriter_fourcc(*'XVID')

#The file is saved in avi format
out = cv2.VideoWriter('output_video.avi',fourcc, 5.1, frameSize)

key_pic = []
#Pictures of Keys
#OCTAVE 1
key_pic.append(cv2.imread("Photos/key_highres.png"))
key_pic.append(cv2.imread("Photos/3D.png"))
key_pic.append(cv2.imread("Photos/3E.png"))
key_pic.append(cv2.imread("Photos/3F.png"))
key_pic.append(cv2.imread("Photos/3G.png"))
key_pic.append(cv2.imread("Photos/3A.png"))
key_pic.append(cv2.imread("Photos/3B.png"))
#OCTAVE 2
key_pic.append(cv2.imread("Photos/2C.png"))
key_pic.append(cv2.imread("Photos/2D.png"))
key_pic.append(cv2.imread("Photos/2E.png"))
key_pic.append(cv2.imread("Photos/2F.png"))
key_pic.append(cv2.imread("Photos/2G.png"))
key_pic.append(cv2.imread("Photos/2A.png"))
key_pic.append(cv2.imread("Photos/2B.png"))
#OCTAVE 3
key_pic.append(cv2.imread("Photos/C.png"))
key_pic.append(cv2.imread("Photos/D.png"))
key_pic.append(cv2.imread("Photos/E.png"))
key_pic.append(cv2.imread("Photos/F.png"))
key_pic.append(cv2.imread("Photos/G.png"))
key_pic.append(cv2.imread("Photos/A.png"))
key_pic.append(cv2.imread("Photos/B.png"))
#OCTAVE 4
key_pic.append(cv2.imread("Photos/C1.png"))
key_pic.append(cv2.imread("Photos/D1.png"))
key_pic.append(cv2.imread("Photos/E1.png"))
key_pic.append(cv2.imread("Photos/F1.png"))
key_pic.append(cv2.imread("Photos/G1.png"))
key_pic.append(cv2.imread("Photos/A1.png"))
key_pic.append(cv2.imread("Photos/B1.png"))
#OCTAVE 5
key_pic.append(cv2.imread("Photos/C2.png"))
key_pic.append(cv2.imread("Photos/D2.png"))
key_pic.append(cv2.imread("Photos/E2.png"))
key_pic.append(cv2.imread("Photos/F2.png"))
key_pic.append(cv2.imread("Photos/G2.png"))
key_pic.append(cv2.imread("Photos/A2.png"))
key_pic.append(cv2.imread("Photos/B2.png"))
#OCTAVE 6
key_pic.append(cv2.imread("Photos/C3.png"))

#FINDING THE THRESHOLD IMAGES OF EACH KEYS
thresh = []

row, column = right_np_arr.shape

base_img2 = base_img.copy()

#Creating the thereshold images for each of the keys
for i in range(len(key_pic)):
	
	gray = cv2.cvtColor(key_pic[i], cv2.COLOR_BGR2GRAY)

	ret, dummy_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

	thresh.append(dummy_thresh)

#Creating a black filter for the base image
img_comp = np.zeros((height,width,3),np.uint8)
base_img = cv2.addWeighted(base_img, 0.5, img_comp, 0.5, 0.0)

#Coloring the keys based on the melody
for i in range(row):
	dummy = base_img.copy()
	for j in range(column):
		if(right_np_arr[i,j]==1):
			dummy[thresh[j]==255] = [180,105,255]
		if(left_np_arr[i,j]==1):
			dummy[thresh[j]==255] = [250,191,0]
	dummy = cv2.addWeighted(base_img, 0.3, dummy, 0.7, 0.0)
	out.write(dummy)

#Saving the video file
out.release()