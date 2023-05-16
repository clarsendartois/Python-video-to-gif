# import libraries
from moviepy.editor import*
from tkinter import *
import tkinter.filedialog as tkfd
import tkinter as tk

window = Tk() # creating window
window.geometry("700x300") # geometry of window
window.title("TechVidvan") # tittle to window
Label(window, text="Let's makw a GIF", font=("bold", 20)).pack() # Label


def browseFiles():
    global filepath
    filename = tkfd.askopenfilenames(title="select", filetypes=[("all video fromat", ".mov"), ("all video fromat", ".flv"), ("all video fromat", ".avi"), ("all video fromat", ".mp4")])
    filepath = os.path.basename(filename)

Label(window, text="Select a File").pack()
Button(window, text="Browse", command=browseFiles).pack() # button field
Button(window, text="Create a Dif").pack()# Button field

# 4. Creating a GIF