from bs4 import BeautifulSoup
import urllib.request
import sys
import numpy as np
from cv2 import cv2
import cv2
import base64
from PIL import Image
import io

def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

base_url = "https://nedrug.mfds.go.kr/pbp/CCBBB01/getItemDetail?itemSeq="
num_url = '200502784'

med_url = base_url + num_url

fp = urllib.request.urlopen(med_url)
source = fp.read()
fp.close()

med_img = BeautifulSoup(source, 'html.parser')
med_img = med_img.find("div",class_ = "pc-img")
# urllib.request.urlretrieve(imgURL,'med.jpg')
# print(med_img)
# print(med_img.find("img")["src"])

imgURL = med_img.find("img")["src"]
# print( type( imgURL ) )
# img64 = imgURL.decode( "base64" )

nparr = np.fromstring(imgURL, np.uint8)
imgnp = cv2.imdecode(nparr, cv2.CV2_LOAD_IMAGE_COLOR)

img_ipl = cv.CreateImageHeader
# img64 = base64.b64decode( imgURL )
#
# imgnp = np.array(img64)
# print(np.shape(imgnp))


# imgdata = base64.b64decode(imgURL)
# image = Image.open(io.BytesIO(imgdata))
# imgimg = stringToRGB(imgURL)
# cv2.imshow("mm", imgnp )
# cv2.waitKey()
# cv2.destroyAllWindows()




