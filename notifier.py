import requests
from bs4 import BeautifulSoup

url= requests.get('https://www.youtube.com/user/UrAvgConsumer')

soup = BeautifulSoup(url.content,"html.parser")

var = soup.find("yt.icon.style")


print(var)