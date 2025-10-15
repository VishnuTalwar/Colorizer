import os
import sys
import subprocess
import ctypes
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import PIL
from PIL import ImageTk, Image

ctypes.windll.shcore.SetProcessDpiAwareness(1)

fixed_height = 600

win = Tk()
win.title("COLORIZER")
win.iconbitmap("wheel.ico")
win.resizable(0,0)
win.minsize(height = fixed_height, width = 1500)
win.config(bg = "#F7C8E0")

style = ttk.Style()
style.theme_use("clam")
style.configure('TButton', background='#865DFF')
style.configure('TButton', foreground='#E384FF')


from file_ui import path1

img1 = Image.open(path1)
img2 = Image.open('colorized_image.jpg')

height_percent = (fixed_height / float(img1.size[1]))
width_size = int((float(img1.size[0]) * float(height_percent)))
res_img = img2.resize((width_size, fixed_height), PIL.Image.NEAREST)
imgtk = ImageTk.PhotoImage(res_img)

height_percent1 = (300 / float(img1.size[1]))
width_size1 = int((float(img1.size[0]) * float(height_percent1)))
sm_img = img1.resize((width_size1, 300))
imsm = ImageTk.PhotoImage(sm_img)

left_frame = Frame(win, width = 400, height = 400, bg = '#ECF9FF',
                       highlightbackground = "#F55050", highlightthickness = 3)
left_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

right_frame = Frame(win, width = 250, height = 250, bg = '#ECF9FF',
                    highlightbackground = "#F55050", highlightthickness = 3)
right_frame.grid(row = 0, column = 1, padx = 10, pady = 10)

lab_txt = Label(left_frame, text = "Original Image", font = ("Copperplate Gothic Bold", 14, 'bold'))
lab_txt.grid(row = 0, column = 0, padx = 5, pady = 5)
lab_txt.config(bg = "#ECF9FF", fg = "#D14D72")

label1 = ttk.Label(left_frame, image = imsm)
label1.image = imsm
label1.grid(row = 1, column = 0, pady = 10, padx = 10)

label2 = ttk.Label(right_frame, image = imgtk)
label2.image = imgtk
label2.pack(padx = 10, pady = 10)

win.grid_columnconfigure(0, weight = 1)
win.grid_columnconfigure(1, weight = 1)


def goback():
    win.destroy()
    subprocess.call([sys.executable] + sys.argv)


img_frame = Frame(left_frame, bg = "#F7C8E0", highlightbackground = "#D14D72", highlightthickness = 3)
img_frame.grid(row = 2, column = 0, pady = 10, padx = 10)


def download():
    filename = filedialog.asksaveasfilename(initialfile = 'Untitled', defaultextension = '.jpg',
                                            filetypes = [("JPEG/JPG File", "*.jpg"), ("PNG File", "*.png"),
                                                         ("All Files", "*.*")])
    imagetri = Image.open("colorized_image.jpg")
    imagetri.save(filename)


bt_dwnld = ttk.Button(img_frame, text = "Save As", command = download)
bt_dwnld.grid(row = 1, column = 1, pady = 10, padx = 10)

goback = ttk.Button(img_frame, text = "Home", command = goback)
goback.grid(row = 1, column = 2, pady = 10, padx = 10)


win.mainloop()

