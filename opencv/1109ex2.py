import sys
import numpy as np
import cv2

def actResize(src):
    size = (1280, 720)
    dst = cv2.resize(src, dsize=size, interpolation=cv2.INTER_AREA)
    return dst

def onMouse(event, x, y, flags, param):

    global pt1
    global pt2
    global pt3
    global pt4
    for i in range(0,4):
        if i == 0:
            if event == cv2.EVENT_LBUTTONDOWN:
                pt1 = x,y
        if i == 1:
            if event == cv2.EVENT_LBUTTONDOWN:
                pt2 = x,y
        if i == 2:
            if event == cv2.EVENT_LBUTTONDOWN:
                pt3 = x,y
        if i == 3:
            if event == cv2.EVENT_LBUTTONDOWN:
                pt4 = x,y

pt1 = []
pt2 = []
pt3 = []
pt4 = []

src = cv2.imread('/home/mango/test/data/test/test.jpg')
src = actResize(src)
if src is None:
    print('Image load failed!')
    sys.exit()
w, h = 360, 180

cv2.setMouseCallback('img', onMouse, [src])

srcQuad = np.array([pt1, pt2, pt3, pt4], np.float32)
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w, h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
