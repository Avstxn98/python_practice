import requests
from bs4 import BeautifulSoup
import re
sr=input("enter word:")

url = "https://dictionary.cambridge.org/dictionary/english/"+str(sr)
sd = requests.get(url)
soup = BeautifulSoup(sd.content,'html.parser')


j = soup.find_all("div",class_="def")

for elements in j:

    print(elements.text)
'''

p = soup.find_all("li", class_="lc")

for element in p:
    print(str(element.list.replace("\n","")))'''

