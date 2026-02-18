import cv2 as cv

img = cv.imread('Photos/face_1.jpg')
cv.cvtColor(img, cv.CALIB_CB_SYMMETRIC_GRID)
cv.imshow('Photo', img)
cv.waitKey(0)
print(type(img))