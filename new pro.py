from tkinter import *
import PIL
from tkinter import filedialog
import time

root = Tk()
root.title('codemy')
root.iconbitmap()
root.geometry("400x400")

# labels

u_label = Label(root, text="hour", font="Calabria")
s_label = Label(root, text="min", font="Calabria")
t_label = Label(root, text="sec", font="Calabria")

# entries
'''u = IntVar()
s = IntVar()
t = IntVar()'''

ut = Entry(root, width=5, borderwidth=5)
st = Entry(root, width=5, borderwidth=5)
tt = Entry(root, width=5, borderwidth=5)


def timer():
    global k
    d = ut.get()
    e = st.get()
    f = tt.get()

    h = d * 3600
    i = e * 60
    j = f * 1
    k = h + i + j

'''ster= IntVar()
ter = IntVar()
ker = IntVar()
fer = IntVar()'''
def timer2():
    global k
    while int(k) >= 0:
        ster, ter = divmod(int(k), 3600)
        ker, fer = divmod(ter, 60)

        int(k) - 1

        time.sleep(1)

        print(ster + ker + fer)
        '''times = Text(root, text=str(ster) + str(ker) + str(fer))
        times.grid(row=13, column=2)'''

# entry positions
u_label.grid(row=5, column=0, padx=(5, 10), pady=5)
s_label.grid(row=5, column=2, padx=(5, 10), pady=5)
t_label.grid(row=5, column=4, padx=(5, 10), pady=5)
ut.grid(row=5, column=1, padx=(5, 10), pady=5)
st.grid(row=5, column=3, padx=(5, 10), pady=5)
tt.grid(row=5, column=5, padx=(5, 10), pady=5)
start_again_button = Button(root, text="START", font="Calabria", command=timer)
end_button = Button(root, text="END", font="Calabria")
pause_resume_button = Button(root, text="P/R", font="Calabria")
start_again2_button = Button(root, text="START", font="Calabria", command=timer2)

# create button positions
pause_resume_button.grid(row=10, column=1, padx=(5, 10), pady=5)
end_button.grid(row=11, column=0, padx=(5, 10), pady=5)
start_again_button.grid(row=10, column=0, padx=(5, 10), pady=5)
start_again2_button.grid(row=12, column=0, padx=(5, 10), pady=5)

root.mainloop()
