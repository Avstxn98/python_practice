from tkinter import *
import PIL
from tkinter import filedialog
import time
import requests
from bs4 import BeautifulSoup
import re

root = Tk()
root.title('codemy')
root.iconbitmap()
root.geometry("650x350")
root.configure(background="Teal")
scrollbar = Scrollbar(root)
headinglabel = Label(root,
                     text="Welcome to the dictionary app. \nMake sure you are connected to the internet when using "
                          "app.\nUse symbol ' - ' for spaces",
                     font="Calabria", bg="teal", fg="white")
headinglabel.grid(row=0, column=1, sticky=W)

l2 = Label(root, text="Enter keyword:", font="Calabria", fg="white", bg="teal")
l2.grid(row=1, column=0, sticky=W)

eed = Entry(root, width=73, borderwidth=5, bg="cadetblue4", fg="white")
eed.grid(row=1, column=1, sticky=W)

# search button
t1 = Text(root, width=50, height=10, bg="mediumpurple1", font="Calabria", fg="white",
          yscrollcommand=scrollbar.set)
t1.grid(row=3, column=1)
t1.configure(xscrollcommand=scrollbar.set)

scrollbar.grid(row=3, column=3, sticky=NS)

scrollbar.configure(command=t1.yview)
# scrollbar.configure(orient=HORIZONTAL)


# radio buttons
rv = StringVar()
rv.set("dictionary")
rb1 = Radiobutton(root, text="Dictionary", variable=rv, value="dictionary", font="Calabria", fg="cyan2").grid(row=2,
                                                                                                              column=0,
                                                                                                              pady=10)
rb2 = Radiobutton(root, text="Thesaurus", variable=rv, value="thesaurus", font="Calabria", fg="cyan2").grid(row=2,
                                                                                                            column=1,
                                                                                                            pady=10)

# search button
sb = Button(root, text="Search", font="Calabria", bg="orchid4", fg="white", command=lambda: r(rv.get()))
sb.grid(row=1, column=2, sticky=W)


def r(value=""):
    rs = []
    rp = []
    if value == "dictionary":
        url = "https://dictionary.cambridge.org/dictionary/english/" + eed.get()
        sd = requests.get(url)
        soup = BeautifulSoup(sd.content, 'html.parser')
        j = soup.find_all("div", class_="def")

        for elements in j:
            t1.delete(0.0, END)
            rp.append(elements.text)
            t1.insert(END, "\n".join(rp))
    elif value == "thesaurus":
        url = "https://dictionary.cambridge.org/dictionary/english/" + eed.get()
        sd = requests.get(url)
        soup = BeautifulSoup(sd.content, 'html.parser')
        p = soup.find_all("li", class_="lc")

        for element in p:
            t1.delete(0.0, END)
            rs.append("".join(element.text.replace("{", "")))
            t1.insert(7.0, "\n".join(rs))

    return


root.mainloop()
