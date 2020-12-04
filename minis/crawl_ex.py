import urllib.request
from bs4 import BeautifulSoup

#웹페이지의 소스를 가져온다.
url = "https://www.kr.playblackdesert.com/BeautyAlbum?searchType=0&searchText=&categoryCode=0&classType=0,4,8,12,16,20,21,24,25,26,28,31,27,19,23,11,29,17,5&Page=1"
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()

#소스에서 img_area 클래스 하위의 소스를 가져온다.
soup = BeautifulSoup(source, 'html.parser')
soup = soup.find("p",class_ = "img_area")

#이미지 경로를 받아온다.
imgURL = soup.find("img")["src"]

print(imgURL)

urllib.request.urlretrieve(imgURL,'00001.jpg')
