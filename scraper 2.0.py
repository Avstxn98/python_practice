from bs4 import BeautifulSoup
import requests
import time
import os
import re
from collections import deque

url = requests.get("https://www.amazon.co.uk/ssd/s?k=ssd")
soup = BeautifulSoup(url.content, 'html.parser')


links= soup.find_all('span')
rs= deque()
for element in links:
    rw= "".join(element.text.replace("\n", " "))
    rs.appendleft(rw)
print(rs)