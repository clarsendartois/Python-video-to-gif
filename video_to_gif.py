import tkinter as tk
import tkinter.filedialog as tkfd
import customtkinter as ctk
from moviepy.editor import VideoFileClip
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

bg_fg_color = "#2b2b2b"


class VideoToGif:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("700x300+0+0")
        self.window.resizable(0, 0)
        self.window.title("CLARSEN: Video To Gif")

        self.frame_display = self.create_frame_display()

    def create_frame_display(self):
        main_frame = ctk.CTkFrame(
            self.window, width=690, height=290, corner_radius=10, fg_color=bg_fg_color)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    video_to_gif = VideoToGif()
    video_to_gif.run()
