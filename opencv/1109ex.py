# 0418.py: OpenCV-Python Tutorials 참조
import cv2
import numpy as np

def actResize(src):
    size = (256, 256)
    dst = cv2.resize(src, dsize=size, interpolation=cv2.INTER_AREA)
    return dst

def actBlur(src):

    dst = cv2.blur(src, (2,2))
    #setting new image's name
    #writing image - dstname = path, dst = image
    return dst

src1 = cv2.imread('/home/mango/test/data/lena.jpg')
src2 = cv2.imread('/home/mango/test/data/test/opencv.jpeg')
cv2.imshow('src2', src2)

src2 = actResize(src2)
#1
rows,cols,channels = src2.shape
roi = src1[0:rows, 0:cols]


#2
gray = cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask',  mask)
cv2.imshow('mask_inv',  mask_inv)

#3
src1_bg = cv2.bitwise_and(roi, roi, mask = mask)
cv2.imshow('src1_bg',  src1_bg)

#4
src2_fg = cv2.bitwise_and(src2, src2, mask = mask_inv)
cv2.imshow('src2_fg',  src2_fg)

#5
##dst = cv2.add(src1_bg, src2_fg)
dst = cv2.bitwise_or(src1_bg, src2_fg)
cv2.imshow('dst',  dst)
dst = actBlur(dst)

#6
src1[0:rows, 0:cols] = dst

cv2.imshow('result',src1)
cv2.waitKey(0)
cv2.destroyAllWindows()
