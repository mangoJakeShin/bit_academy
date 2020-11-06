import cv2

path = "/home/mango/test/data/lena.jpg"
src = cv2.imread(path)

dst = src.copy()
dst = src[100:600, 200:700]

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()