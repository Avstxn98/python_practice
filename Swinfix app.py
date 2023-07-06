from tkinter import *
from tkinter import filedialog
import time
import requests
from bs4 import BeautifulSoup
import re
from collections import deque
import sqlite3 as sq
from tkinter import filedialog

root = Tk()
root.title('Swinfix inventory app')
root.iconbitmap()
root.configure(background="Teal")


# commands for buttons
def deletea():
    cpu_t.delete(0.0, END)
    gpu_t.delete(0.0, END)
    psu_t.delete(0.0, END)
    cpucooler_t.delete(0.0, END)
    motherboard_t.delete(0.0, END)
    ram_t.delete(0.0, END)
    storage_t.delete(0.0, END)
    storage2_t.delete(0.0, END)
    case_t.delete(0.0, END)
    customer_budget_t.delete(0.0, END)
    customer_name_t.delete(0.0, END)
    return


# edit box
def editb():
    top = Toplevel()
    top.configure(background="Teal")
    deletebutlab = Label(top, text="CUSTOMER ID", font="Calabria", bg="orchid4", fg="white").grid(row=1, column=0,
                                                                                                  sticky=W, padx=5,
                                                                                                  pady=5)
    deletebut = Entry(top, width=73, borderwidth=5, bg="cadetblue4", fg="white")
    deletebut.grid(row=1, column=1, sticky=W)

    global data

    # noinspection PyGlobalUndefined
    def showdb():
        bottom = Toplevel()
        conn = sq.connect('swinfix2_files.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM swinfix2")
        records = c.fetchall()

        # loop through results
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        conn.commit()
        conn.close()

        data = Label(bottom, font="Calabria", text=print_records, bg="orchid4", fg="white")
        data.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        # def can():
        # data.destroy()
        # return

        # data.after(300000, can)

    def removeb():
        conn = sq.connect('swinfix2_files.db')
        c = conn.cursor()
        c.execute("DELETE from swinfix2 WHERE oid=" + deletebut.get())
        deletebut.forget()

        conn.commit()
        conn.close()
        return

    def mchgs():
        customer_budget_t.delete(0.0, END)
        customer_name_t.delete(0.0, END)
        cpu_t.delete(0.0, END)
        gpu_t.delete(0.0, END)
        psu_t.delete(0.0, END)
        cpucooler_t.delete(0.0, END)
        motherboard_t.delete(0.0, END)
        ram_t.delete(0.0, END)
        storage_t.delete(0.0, END)
        storage2_t.delete(0.0, END)
        case_t.delete(0.0, END)
        conn = sq.connect('swinfix2_files.db')
        c = conn.cursor()
        c.execute("SELECT * FROM swinfix2 where oid=" + str(deletebut.get()))
        records = c.fetchall()

        for record in records:
            cpu_t.insert(0.0, record[2])
            gpu_t.insert(0.0, record[3])
            psu_t.insert(0.0, record[4])
            motherboard_t.insert(0.0, record[5])
            cpucooler_t.insert(0.0, record[6])
            ram_t.insert(0.0, record[7])
            storage_t.insert(0.0, record[8])
            storage_t.insert(0.0, record[9])
            case_t.insert(0.0, record[10])
            customer_name_t.insert(0.0, record[0])
            customer_budget_t.insert(0.0, record[1])

        top.destroy()
        return

    mch = Button(top, text="MAKE CHANGES", font="Calabria", bg="orchid4", fg="white", command=lambda: mchgs(), padx=49,
                 pady=7)
    mch.grid(row=2, column=2, padx=5, pady=5)

    deletedata = Button(top, text="DELETE DATA", font="Calabria", bg="orchid4", fg="white", command=lambda: removeb(),
                        padx=49,
                        pady=7)
    deletedata.grid(row=2, column=1, padx=5, pady=5)
    showd = Button(top, text="SHOW ALL DATA", font="Calabria", bg="orchid4", fg="white", command=lambda: showdb(),
                   padx=49,
                   pady=7)
    showd.grid(row=2, column=0, padx=5, pady=5)


# buttons
save_to_db = Button(root, text="SAVE TO DATABASE", font="Calabria", bg="orchid4", fg="white", padx=55, pady=7,
                    command=lambda: sdb())
save_to_db.grid(row=17, column=2, sticky=E, padx=5, pady=5)

createf = Button(root, text="CREATE DOC", font="Calabria", bg="orchid4", fg="white", padx=55, pady=7,
                 command=lambda: crf())
createf.grid(row=17, column=0, sticky=W, padx=5, pady=5)

delete_all = Button(root, text="DELETE ALL", font="Calabria", bg="orchid4", fg="white", padx=55, pady=7,
                    command=lambda: deletea())
delete_all.grid(row=17, column=1, padx=5, pady=5)

cpu = Button(root, text="CPU", font="Calabria", bg="orchid4", fg="white", padx=55, pady=7, command=lambda: cpu_b())
cpu.grid(row=1, column=0, sticky=W, pady=5, padx=5)

gpu = Button(root, text="GPU", font="Calabria", bg="orchid4", fg="white", padx=55, pady=7, command=lambda: gpu_b())
gpu.grid(row=1, column=1)

psu = Button(root, text="PSU", font="Calabria", bg="orchid4", fg="white", command=lambda: psu_b(), padx=55, pady=7)
psu.grid(row=1, column=2, padx=5, pady=5)

cpu_cooler = Button(root, text="CPU_COOLER", font="Calabria", bg="orchid4", fg="white", command=lambda: cpu_cooler(),
                    padx=17, pady=7)
cpu_cooler.grid(row=2, column=0, sticky=W, padx=5, pady=5)

ram = Button(root, text="RAM", font="Calabria", bg="orchid4", fg="white", command=lambda: ram_b(), padx=54, pady=7)
ram.grid(row=2, column=1, padx=5, pady=5)

motherboard = Button(root, text="MOTHERBOARD", font="Calabria", bg="orchid4", fg="white",
                     command=lambda: motherboard_b(),
                     padx=10, pady=7)
motherboard.grid(row=2, column=2, padx=5, pady=5)

storage = Button(root, text="STORAGE", font="Calabria", bg="orchid4", fg="white", command=lambda: storage_b(), padx=33,
                 pady=7)
storage.grid(row=3, column=0, sticky=W, padx=5, pady=5)

storage2 = Button(root, text="STORAGE2", font="Calabria", bg="orchid4", fg="white", command=lambda: storage_b2(),
                  padx=33,
                  pady=7)
storage2.grid(row=3, column=2, sticky=W, padx=5, pady=5)

case = Button(root, text="CASE", font="Calabria", bg="orchid4", fg="white", command=lambda: case_b(), padx=49,
              pady=7)
case.grid(row=3, column=1, padx=5, pady=5)

edit = Button(root, text="EDIT DB", font="Calabria", bg="orchid4", fg="white", command=lambda: editb(), padx=49,
              pady=7)
edit.grid(row=18, column=2, padx=5, pady=5)

# website collection


# new windows

'''cpu'''
intelrs = deque()
amdo = []
# amd
cpul = requests.get("https://en.wikipedia.org/wiki/List_of_AMD_Ryzen_microprocessors")
soupcpu = BeautifulSoup(cpul.text, "html.parser")
linkscpu = soupcpu.find_all("th")

for amd in linkscpu:

    if amd.text[0] == "R":
        amdrw = "".join(amd.text.replace("{", ""))
        amdo.append(amdrw)

# INTEL
intel = requests.get("https://en.wikipedia.org/wiki/List_of_Intel_microprocessors")
soupintel = BeautifulSoup(intel.text, 'html.parser')
linksintel = soupintel.find_all(class_='external text')

inte = []
for int in linksintel:
    ru = "".join(int.text.replace("{", ""))
    intelrs.appendleft(ru)
for elemente in intelrs:
    inte.append(elemente)
del inte[0:27]


def cpu_b():
    top = Toplevel()
    top.configure(background="Teal")
    clicked = StringVar()

    # AMD

    # save command
    def add():
        cpu_t.insert(0.0, clicked.get())
        top.destroy()

    # button and menu
    saveb = Button(top, text="save", command=add)
    saveb.grid(row=3, column=2)

    drop = OptionMenu(top, clicked, *amdo)
    drop.grid(row=1, column=2)
    drop2 = OptionMenu(top, clicked, *inte)
    drop2.grid(row=2, column=2)
    # label
    Label(top, text="INTEL").grid(row=2, column=0)
    Label(top, text="AMD").grid(row=1, column=0)


# gpu
nvidia = []
radeon = []

# AMD
vrradeon = requests.get("https://www.techpowerup.com/gpu-specs/?mfgr=AMD&mobile=No&sort=released")
soupradeon = BeautifulSoup(vrradeon.text, "html.parser")
linksradeon = soupradeon.find_all(class_="vendor-AMD")

for elements in linksradeon:
    rad = "".join(elements.text.replace("\n", ""))
    radeon.append(rad)

# NVIDIA
urlnvidia = requests.get("https://www.techpowerup.com/gpu-specs/?mfgr=NVIDIA&mobile=No&sort=released")
soupnvidia = BeautifulSoup(urlnvidia.text, 'html.parser')
linksnvidia = soupnvidia.find_all(class_="vendor-NVIDIA")
for element in linksnvidia:
    nvid = "".join(element.text.replace("\n", ""))
    nvidia.append(nvid)


def gpu_b():
    tv = Toplevel()
    tv.configure(background="Teal")

    clicked = StringVar()

    # save command
    def add():
        gpu_t.insert(0.0, clicked.get())
        tv.destroy()

    # button and menu
    saveb = Button(tv, text="save", command=add)
    saveb.grid(row=3, column=2)

    drop = OptionMenu(tv, clicked, *radeon)
    drop.grid(row=1, column=2)
    drop2 = OptionMenu(tv, clicked, *nvidia)
    drop2.grid(row=2, column=2)
    # label
    Label(tv, text="NVIDIA").grid(row=2, column=0)
    Label(tv, text="AMD").grid(row=1, column=0)

    return


# psu
urlpsu = requests.get("https://www.scan.co.uk/shop/computer-hardware/cases/all")

souppsu = BeautifulSoup(urlpsu.content, 'html.parser')

linkspsu = souppsu.find_all('span', class_="description")
rspsu = deque()

for elementpsu in linkspsu:
    rtpsu = elementpsu.find("a")

    rspsu.appendleft(rtpsu.text)

fdpsu = []
for elementepsu in rspsu:
    fdpsu.append(elementepsu)
del fdpsu[0:84]


def psu_b():
    remote = Toplevel()
    remote.configure(background="Teal")

    def add():
        storage_t.insert(0.0, clicked.get())
        remote.destroy()

    # button and menu
    saveb = Button(remote, text="save", command=add)
    saveb.grid(row=3, column=2)
    clicked = StringVar()

    drop2 = OptionMenu(remote, clicked, *fdpsu)
    drop2.grid(row=1, column=2)
    # label

    Label(remote, text="PSU").grid(row=1, column=0)
    return


# cpu cooler
# water cooler
urlwat = requests.get("https://www.scan.co.uk/shop/computer-hardware/cooling-water/all")

soupwat = BeautifulSoup(urlwat.content, 'html.parser')

linkswat = soupwat.find_all('span', class_="description")
rswat = deque()

for elementwat in linkswat:
    rtwat = elementwat.find("a")

    rswat.appendleft(rtwat.text)

fdwat = []
for elementewat in rswat:
    fdwat.append(elementewat)
del fdwat[0:284]

# air cooler
vmair = deque()
vrmair = requests.get("https://www.scan.co.uk/shop/computer-hardware/cooling-air/all")

soup2air = BeautifulSoup(vrmair.text, "html.parser")
links2air = soup2air.find_all('span', class_="description")
for elementsair in links2air:
    vrair = elementsair.find("a")
    vmair.appendleft(vrair.text)

veair = []
for elemeair in vmair:
    veair.append(elemeair)
del veair[0:66]


def cpu_cooler():
    ice = Toplevel()
    ice.configure(background="Teal")

    def add():
        cpucooler_t.insert(0.0, clicked.get())
        ice.destroy()

    # button and menu
    saveb = Button(ice, text="save", command=add)
    saveb.grid(row=3, column=2)
    clicked = StringVar()

    drop = OptionMenu(ice, clicked, *veair)
    drop.grid(row=1, column=2)
    drop2 = OptionMenu(ice, clicked, *fdwat)
    drop2.grid(row=2, column=2)
    # label
    Label(ice, text="WATER COOLING").grid(row=2, column=0)
    Label(ice, text="AIR COOLING").grid(row=1, column=0)

    return


# ram

urlram = requests.get("https://www.scan.co.uk/shop/computer-hardware/memory-ram/all")

soupram = BeautifulSoup(urlram.content, 'html.parser')

linksram = soupram.find_all('span', class_="description")
rsram = deque()

for elementram in linksram:
    rtram = elementram.find("a")

    rsram.appendleft(rtram.text)

fdram = []
for eleram in rsram:
    fdram.append(eleram)
del fdram[0:5]


def ram_b():
    mem = Toplevel()
    mem.configure(background="Teal")

    def add():
        ram_t.insert(0.0, clicked.get())
        mem.destroy()

    # button and menu
    saveb = Button(mem, text="save", command=add)
    saveb.grid(row=3, column=2)
    clicked = StringVar()

    drop2 = OptionMenu(mem, clicked, *fdram)
    drop2.grid(row=2, column=1)
    # label
    Label(mem, text="RAM").grid(row=2, column=0)

    return


# motherboard
# intel
urlmotherintel = requests.get("https://www.scan.co.uk/shop/computer-hardware/motherboards-intel/all")

soupmotherintel = BeautifulSoup(urlmotherintel.content, 'html.parser')

linksmotherintel = soupmotherintel.find_all('span', class_="description")
rsmotherintel = deque()

for elementmointel in linksmotherintel:
    rtmothintel = elementmointel.find("a")

    rsmotherintel.appendleft(rtmothintel.text)

fd = []
for elmotherintel in rsmotherintel:
    fd.append(elmotherintel)
del fd[0:65]

# amd
vmmotheramd = deque()
vrmmotheramd = requests.get("https://www.scan.co.uk/shop/computer-hardware/motherboards-amd/all")

soup2motheramd = BeautifulSoup(vrmmotheramd.text, "html.parser")
links2mothamd = soup2motheramd.find_all('span', class_="description")
for elmotheramd in links2mothamd:
    vrma = elmotheramd.find("a")
    vmmotheramd.appendleft(vrma.text)

vema = []
for elma in vmmotheramd:
    vema.append(elma)
del vema[0:104]


def motherboard_b():
    sister = Toplevel()
    sister.configure(background="Teal")

    def add():
        motherboard_t.insert(0.0, clicked.get())
        sister.destroy()

    # button and menu
    saveb = Button(sister, text="save", command=add)
    saveb.grid(row=3, column=2)
    clicked = StringVar()

    drop = OptionMenu(sister, clicked, *vema)
    drop.grid(row=1, column=2)
    drop2 = OptionMenu(top, clicked, *fd)
    drop2.grid(row=2, column=2)
    # label
    Label(sister, text="INTEL").grid(row=2, column=0)
    Label(sister, text="AMD").grid(row=1, column=0)
    return


# storage
# ssd
url = requests.get("https://www.scan.co.uk/shop/computer-hardware/hard-drives-internal/all")

soup = BeautifulSoup(url.content, 'html.parser')

links = soup.find_all('span', class_="description")
rs = deque()

for element in links:
    rt = element.find("a")

    rs.appendleft(rt.text)
eat = []
for elemente in rs:
    eat.append(elemente)
del eat[0:244]

# hdd
vm = deque()
vrm = requests.get("https://www.scan.co.uk/shop/computer-hardware/solid-state-drives/all")

soup2 = BeautifulSoup(vrm.text, "html.parser")
links2 = soup2.find_all('span', class_="description")
for elements in links2:
    vr = elements.find("a")
    vm.appendleft(vr.text)
ve = []
for elemente in vm:
    ve.append(elemente)
del ve[0:244]


def storage_b():
    top = Toplevel()
    top.configure(background="Teal")
    top.geometry("650x350")

    def add():
        storage_t.insert(0.0, clicked.get())
        top.destroy()

    # button and menu
    saveb = Button(top, text="save", command=add)
    saveb.grid(row=3, column=2)
    clicked = StringVar()

    drop = OptionMenu(top, clicked, *ve)
    drop.grid(row=1, column=2)
    drop2 = OptionMenu(top, clicked, *eat)
    drop2.grid(row=2, column=2)
    # label
    Label(top, text="HDD").grid(row=2, column=0)
    Label(top, text="SSD").grid(row=1, column=0)
    return


def storage_b2():
    top = Toplevel()
    top.configure(background="Teal")
    top.geometry("650x350")

    def add():
        storage2_t.insert(0.0, clicked.get())
        top.destroy()

    # button and menu
    saveb = Button(top, text="save", command=add)
    saveb.grid(row=3, column=2)
    clicked = StringVar()

    drop = OptionMenu(top, clicked, *ve)
    drop.grid(row=1, column=2)
    drop2 = OptionMenu(top, clicked, *eat)
    drop2.grid(row=2, column=2)
    # label
    Label(top, text="HDD").grid(row=2, column=0)
    Label(top, text="SSD").grid(row=1, column=0)
    return


# case
urlc = requests.get("https://www.scan.co.uk/shop/computer-hardware/cases/all")

soupc = BeautifulSoup(urlc.content, 'html.parser')

linksc = soupc.find_all('span', class_="description")
rsc = deque()

for elementc in linksc:
    rtc = elementc.find("a")

    rsc.appendleft(rtc.text)

fdc = []
for elementec in rsc:
    fdc.append(elementec)
del fdc[0:44]


def case_b():
    top = Toplevel()
    top.configure(background="Teal")

    def add():
        case_t.insert(0.0, clicked.get())
        top.destroy()

    # button and menu
    saveb = Button(top, text="save", command=add)
    saveb.grid(row=3, column=2)
    clicked = StringVar()

    drop2 = OptionMenu(top, clicked, *fd)
    drop2.grid(row=1, column=2)
    # label

    Label(top, text="CASE").grid(row=1, column=0)
    return


# checkbox

# textbox
cpu_t = Text(root, width=30, height=1, bg="mediumpurple1", font="Calabria", fg="white")
cpu_t.grid(row=6, column=1, padx=5, pady=5)

gpu_t = Text(root, width=30, height=1, bg="mediumpurple1", font="Calabria", fg="white")
gpu_t.grid(row=7, column=1, padx=5, pady=5)

psu_t = Text(root, width=30, height=1, bg="mediumpurple1", font="Calabria", fg="white")
psu_t.grid(row=8, column=1, padx=5, pady=5)

cpucooler_t = Text(root, width=30, height=1, bg="mediumpurple1", font="Calabria", fg="white")
cpucooler_t.grid(row=9, column=1, padx=5, pady=5)

motherboard_t = Text(root, width=30, height=1, bg="mediumpurple1", font="Calabria", fg="white")
motherboard_t.grid(row=10, column=1, padx=5, pady=5)

ram_t = Text(root, width=30, height=1, bg="mediumpurple1", font="Calabria", fg="white")
ram_t.grid(row=11, column=1, padx=5, pady=5)

storage_t = Text(root, width=30, height=1, bg="mediumpurple1", font="Calabria", fg="white")
storage_t.grid(row=12, column=1, padx=5, pady=5)

storage2_t = Text(root, width=30, height=1, bg="mediumpurple1", font="Calabria", fg="white")
storage2_t.grid(row=12, column=1, padx=5, pady=5)

case_t = Text(root, width=30, height=1, bg="mediumpurple1", font="Calabria", fg="white")
case_t.grid(row=13, column=1, padx=5, pady=5)

customer_name_t = Text(root, width=30, height=1, bg="mediumpurple1", font="Calabria", fg="white")
customer_name_t.grid(row=14, column=1, padx=5, pady=5)

customer_budget_t = Text(root, width=30, height=1, bg="mediumpurple1", font="Calabria", fg="white")
customer_budget_t.grid(row=15, column=1, padx=5, pady=5)

# label
cpu_label = Label(root, text="CPU:", font="Calabria", bg="orchid4", fg="white").grid(row=6, column=0, sticky=W, padx=5,
                                                                                     pady=5)
gpu_label = Label(root, text="GPU:", font="Calabria", bg="orchid4", fg="white").grid(row=7, column=0, sticky=W, padx=5,
                                                                                     pady=5)
psu_label = Label(root, text="PSU:", font="Calabria", bg="orchid4", fg="white").grid(row=8, column=0, sticky=W, padx=5,
                                                                                     pady=5)
cpucooler_label = Label(root, text="CPU COOLER:", font="Calabria", bg="orchid4", fg="white").grid(row=9, column=0,
                                                                                                  sticky=W, padx=5,
                                                                                                  pady=5)
motherboard_label = Label(root, text="MOTHERBOARD:", font="Calabria", bg="orchid4", fg="white").grid(row=10, column=0,
                                                                                                     sticky=W, padx=5,
                                                                                                     pady=5)
ram_label = Label(root, text="RAM:", font="Calabria", bg="orchid4", fg="white").grid(row=11, column=0, sticky=W, padx=5,
                                                                                     pady=5)
storage_label = Label(root, text="STORAGE:", font="Calabria", bg="orchid4", fg="white").grid(row=12, column=0,
                                                                                             sticky=W, padx=5, pady=5)

storage_label2 = Label(root, text="STORAGE:", font="Calabria", bg="orchid4", fg="white").grid(row=13, column=0,
                                                                                              sticky=W, padx=5, pady=5)
case_label = Label(root, text="CASE:", font="Calabria", bg="orchid4", fg="white").grid(row=14, column=0,
                                                                                       sticky=W, padx=5, pady=5)
customer_name_label = Label(root, text="CUSTOMER NAME", font="Calabria", bg="orchid4", fg="white").grid(row=15,
                                                                                                        column=0,
                                                                                                        sticky=W,
                                                                                                        padx=5, pady=5)
customer_budget_label = Label(root, text="CUSTOMER BUDGET", font="Calabria", bg="orchid4", fg="white").grid(row=16,
                                                                                                            column=0,
                                                                                                            sticky=W,
                                                                                                            padx=5,
                                                                                                            pady=5)


# database
def sdb():
    conn = sq.connect('swinfix2_files.db')
    c = conn.cursor()
    c.execute(
        "CREATE TABLE  IF NOT EXISTS swinfix2 (customer_name TEXT,customer_budget INTEGER,cpu TEXT,gpu TEXT,psu TEXT,cpu_cooler TEXT,motherboard TEXT,ram TEXT,storage TEXT,storage_2 TEXT, casE_ TEXT)")
    c.execute("""INSERT INTO swinfix2 VALUES(
    :customer_name,
    :customer_budget,
    :cpu,
    :gpu,
    :psu,
    :cpu_cooler,
    :motherboard,
    :ram,:storage,
    :storage_2,
    :case)""",
              {'customer_name': customer_name_t.get(0.0, END), 'customer_budget': customer_budget_t.get(0.0, END),
               'cpu': cpu_t.get(0.0, END),
               'gpu': gpu_t.get(0.0, END), 'cpu_cooler': cpucooler_t.get(0.0, END), 'psu': psu_t.get(0.0, END),
               'motherboard': motherboard_t.get(0.0, END), 'ram': ram_t.get(0.0, END),
               'storage': storage_t.get(0.0, END), 'storage_2': storage2_t.get(0.0, END),
               'case': case_t.get(0.0, END)}
              )

    conn.commit()
    conn.close()

    cpu_t.delete(0.0, END)
    gpu_t.delete(0.0, END)
    psu_t.delete(0.0, END)
    cpucooler_t.delete(0.0, END)
    motherboard_t.delete(0.0, END)
    ram_t.delete(0.0, END)
    storage_t.delete(0.0, END)
    storage2_t.delete(0.0, END)
    case_t.delete(0.0, END)
    return


# sliders


# status bar

# file opener
cmt = str(customer_name_t.get(0.0, END)).replace(" \n", "_")


def crf():
    with open(" str(customer_name_t.get(0.0, END)).txt", "w") as cms:
        cms.write("CUSTOMER NAME: " + customer_name_t.get(0.0, END))
        cms.write("CUSTOMER BUDGET: " + customer_budget_t.get(0.0, END))
        cms.write("CPU: " + cpu_t.get(0.0, END))
        cms.write("GPU: " + gpu_t.get(0.0, END))
        cms.write("PSU: " + psu_t.get(0.0, END))
        cms.write("CPU COOLER: " + cpucooler_t.get(0.0, END))
        cms.write("MOTHERBOARD: " + motherboard_t.get(0.0, END))
        cms.write("RAM: " + ram_t.get(0.0, END))
        cms.write("STORAGE:" + storage_t.get(0.0, END))
        cms.write("STORAGE 2:" + storage2_t.get(0.0, END))
        cms.write("CASE: " + case_t.get(0.0, END))


root.mainloop()
