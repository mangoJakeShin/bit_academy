from Advancedlanefinding.calibration import *
import numpy as np
import cv2
import os

imageFile = '/home/mango/test/Advancedlanefinding/img/'
imglist = os.listdir(imageFile)
mtx, dist = calib()

for i in imglist:
    newimg = os.path.join(imageFile,i)
    if os.path.isfile(newimg):
        src = cv2.imread(newimg)
        cv2.imshow('%s'%i,src)
        srcResult = undistort(src, mtx, dist)
        cv2.imshow("srcresult", srcResult)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("fail")






