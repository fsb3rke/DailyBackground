# AUTHOR: BERKE (fsb3rke)

import tkinter as tkr
import os
import ctypes
import json

class LANGUAGE:
    languages = {"tr": "tr", "en": "en"}
    class TITLE:
        class TR:
            title: str = "Günlük Arkaplan Resim Seçici"
        class EN:
            title: str = "Daily Background Image Select"
    class BUTTON:
        class TR:
            text: str = "Arkaplan Resmini Değiştir"
        class EN:
            text: str = "Set Background Image"

current_directory = os.getcwd()
os.chdir("..")
settings = json.loads(open("settings.json", "r").read())
os.chdir(current_directory)
image_select = tkr.Tk()
title_text: str = ""
if settings["language"] == LANGUAGE.languages["en"]:
    title_text = LANGUAGE.TITLE.EN.title
elif settings["language"] == LANGUAGE.languages["tr"]:
    title_text = LANGUAGE.TITLE.TR.title
image_select.title(title_text)
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

button_text: str = ""
if settings["language"] == LANGUAGE.languages["en"]:
    button_text = LANGUAGE.BUTTON.EN.text
elif settings["language"] == LANGUAGE.languages["tr"]:
    button_text = LANGUAGE.BUTTON.TR.text
set_background_button = tkr.Button(image_select, width=5, height=3, font="Helvetica 12 bold", text=button_text, command=set_background_image, bg="black", fg="white")
var = tkr.StringVar() 
image_title = tkr.Label(image_select, font="Helvetica 12 bold", textvariable=var)

image_title.pack()
image_name_list.pack(fill="both", expand="yes")
set_background_button.pack(fill="x")

image_select.mainloop()
