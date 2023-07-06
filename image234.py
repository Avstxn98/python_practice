from tkinter import *
import PIL
from tkinter import filedialog

root = Tk()
root.title('codemy')
root.iconbitmap()
root.geometry("600x1000")

def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="/", title="open file", filetypes=(("png files","*.png"),("jpeg files","*.jpg")))
    Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    Label(image=my_img).pack()


btn = Button(root, text="open file", command=open).pack()

root.mainloop()
