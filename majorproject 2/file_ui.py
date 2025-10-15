import os
import sys
import ctypes
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import PIL
from PIL import ImageTk, Image

ctypes.windll.shcore.SetProcessDpiAwareness(1)

fixed_height = 600

root = Tk()
root.title("COLORIZER")
root.iconbitmap("wheel.ico")
root.resizable(0,0)
root.minsize(height = fixed_height, width = 1500)
root.config(bg = "#F7C8E0")

style = ttk.Style()
style.theme_use("clam")
style.configure('TButton', background='#865DFF')
style.configure('TButton', foreground='#E384FF')

path1 = ''
img_frame = ''


def start():
    global path1
    global img_frame

    def select():
        global path1
        filename = filedialog.askopenfilename(filetypes = [("Image File",'.jpg .png .jpeg')])
        path1 = str(filename)

    def submit():
        global img_frame

        if path1:
            bt_submit.destroy()
            bt_select.destroy()
            ui_label.destroy()
            ui_head.destroy()
            ui_frame.destroy()
            ui_frame_text.destroy()
            ui_button_Frame.destroy()
            root.destroy()

        else:
            lpath = Label(ui_button_Frame, text = "Select folder !")
            lpath.grid(row = 2, column = 0, padx = 10, pady = 10)
            lpath.config(bg = "#F7C8E0", fg = "#865DFF")

    ui_head = Label(text = "COLORIZER", font = ("Copperplate Gothic Bold",40))
    ui_head.pack(side = TOP, pady = 10, padx = 10)
    ui_head.config(bg = "#F7C8E0", fg = "#865DFF")

    ui_frame = Frame(root, width = 1200, height = fixed_height-100)
    ui_frame.place(anchor = CENTER, rely = 0.5, relx = 0.5)
    ui_frame.config(bg = "#F7C8E0", highlightbackground = "#F55050", highlightthickness = 3)

    ui_frame_text = Frame(ui_frame, width = 1200, height = fixed_height-100)
    ui_frame_text.grid(row = 0, column = 0)
    ui_frame_text.config(bg = "#F7C8E0", highlightbackground = "#F55050")

    ui_label = Label(ui_frame_text, text = "Select the image to be colorized", font = ("Copperplate Gothic Bold",18))
    ui_label.grid(row = 0, column = 1, pady = 10, padx = 10)
    ui_label.config(bg = "#F7C8E0", fg = "#865DFF")

    ui_button_Frame = Frame(ui_frame, width = 1200, height = fixed_height-100)
    ui_button_Frame.grid(row = 1, column = 0)
    ui_button_Frame.config(bg = "#F7C8E0", highlightbackground = "#F55050")

    bt_select = ttk.Button(ui_button_Frame, text = 'Browse', command = select)
    bt_select.grid(row = 1, column = 0, pady = 10, padx = 10)

    bt_submit = ttk.Button(ui_button_Frame, text = "Submit", command = submit)
    bt_submit.grid(row = 1, column = 1, pady = 10, padx = 10)


start()
root.mainloop()

