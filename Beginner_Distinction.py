import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

bozu = cv.imread("Media/Bozu.png")
galaxy = cv.imread("Media/galaxy.jpg")
frame = cv.imread("Media/gold_frame.jpg")
frame_h, frame_w = frame.shape[:2]
bozu_h, bozu_w = bozu.shape[0:2]

# Headshot bozu
head_shot = bozu[0:450, :]

# Photoframe bozu
# Blue padding
constant = 100
border = np.zeros((bozu_h+constant, bozu_w+constant, 3), dtype="uint8")
border[:] = (0, 0, 255)

offset = round(constant/2)
border[offset:bozu_h+offset, offset:bozu_w+offset] = bozu

# Gold frame
frame_h, frame_w = frame.shape[:2]

x_offset = round((frame_h - bozu_h)/2)
y_offset = round((frame_w - bozu_w)/2)

frame[x_offset:bozu_h+x_offset, y_offset:bozu_w+y_offset] = bozu

# Galaxy bozu
x, y = 800, 200
galaxy[y:bozu_h + y, x:bozu_w + x] = bozu

cv.imwrite("Beginner Distinction/Bozu_headshot.jpg", head_shot)
cv.imwrite("Beginner Distinction/Galaxy_bozu.jpg", galaxy)
cv.imwrite("Beginner Distinction/Bozu_frame_1.jpg", border)
cv.imwrite("Beginner Distinction/Bozu_frame_2.jpg", frame)
