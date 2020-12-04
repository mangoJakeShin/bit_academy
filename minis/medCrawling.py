from bs4 import BeautifulSoup as soup
import urllib.request


base_url = "https://nedrug.mfds.go.kr/pbp/CCBBB01/getItemDetail?itemSeq="
num_url = '200502784'

soup = soup.find("div",class_ = "pc-img")




