import requests
from bs4 import BeautifulSoup
import pyautogui
arv = "https://en.wikipedia.org/wiki/Special:Random"
uv = requests.get(arv)

soup = BeautifulSoup(uv.content, 'lxml')
b = soup.find('h1')
for element in b:
    print(element.replace("<", " "))

req = input("Do you want to read article? ")

if req == 'yes':
    p = soup.find_all('p')

    for element in p:
        print(element.text.replace("<", " "))
elif req == 'no':
    while req == 'no':
        arv = "https://en.wikipedia.org/wiki/Special:Random"
        uv = requests.get(arv)

        soup = BeautifulSoup(uv.content, 'lxml')
        pyautogui.hotkey('f5')

        b = soup.find('h1')
        for element in b:
            print(element.replace("<", " "))
        req = input("Do you want to read article? ")
        if req == 'yes':
            p = soup.find_all('p')
            for element in p:
                print(element.text.replace("<", " "))
                break

elif req == 'exit':
    del soup
