import tkinter as tkr
import os
import ctypes

image_select = tkr.Tk()
image_select.title("Daily Background Image Select") 
image_select.geometry("450x350")
image_select.iconbitmap("../bin/icon.ico")
image_select.iconphoto
directory = "../images"
os.chdir(directory)
image_list = os.listdir()

image_name_list = tkr.Listbox(image_select, font="Helvetica 12 bold", bg="lightgray", selectmode=tkr.SINGLE)
for item in image_list:
    pos = 0
    image_name_list.insert(pos, item)
    pos += 1

def set_background_image():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{os.getcwd()}\\{image_name_list.get(tkr.ACTIVE)}", 0)
    var.set(image_name_list.get(tkr.ACTIVE))

set_background_button = tkr.Button(image_select, width=5, height=3, font="Helvetica 12 bold", text="Set Background Image", command=set_background_image, bg="black", fg="white")
var = tkr.StringVar() 
image_title = tkr.Label(image_select, font="Helvetica 12 bold", textvariable=var)

image_title.pack()
image_name_list.pack(fill="both", expand="yes")
set_background_button.pack(fill="x")

image_select.mainloop()
