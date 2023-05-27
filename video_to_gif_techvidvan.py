#import libraries
from moviepy.editor import *
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os

window = Tk()  # creating window
window.geometry('700x300')  # geomtry of window
window.title('TechVidvan')  # title to window
Label(window, text="Let's make a GIF", font=('bold', 20)).pack()  # label


# def browseFiles():
#     global filepath
#     filename = filedialog.askopenfilenames(title='select', filetypes=[
#         ("all video format", ".mov"),
#         ("all video format", ".flv"),
#         ("all video format", ".avi"),
#         ("all video format", ".mp4"),
#     ])
#     filepath = os.path.basename(filename)


def browseFiles():
    global filepath
    file = filedialog.askopenfile(title='select', mode="r", filetypes=[
        ("all video format", ".mov"),
        ("all video format", ".flv"),
        ("all video format", ".avi"),
        ("all video format", ".mp4"),
    ])

    filepath = os.path.abspath(file.name)

    # if file:
    #     filepath = os.path.abspath(file.name)
    #     Label(window, text="The File is located at : " +
    #           str(filepath), font=('Aerial 11')).pack()


def create_gif():
    clip = VideoFileClip(filepath)
    clip.write_gif("./test/test3.gif", fps=10)  # making a gif
    # gif = VideoFileClip(".//test1.gif", fps=10)
    Label(window, text="Gif Created and Saved").pack()


Label(window, text='Select a File').pack()
Button(window, text='Browse', command=browseFiles).pack()  # button field
Button(window, text='Create a Gif', command=create_gif,
       bg='yellow').pack()  # button field

window.mainloop()  # display window
