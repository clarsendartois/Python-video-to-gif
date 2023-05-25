import tkinter as tk
import tkinter.filedialog as tkfd
import customtkinter as ctk
from moviepy.editor import VideoFileClip
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

font_style_text1 = ("Bookman Old Style", 60, "bold")
font_style_text2 = ("Bookman Old Style", 30)
font_style_button1 = ("Bookman Old Style", 25, "bold")
font_style_button2 = ("Bookman Old Style", 40, "bold")


bg_fg_color = "#2b2b2b"
text_color = "#FFFFFF"
text_button1_color = "#f97583"
text_button1_color2 = "#37b78f"


text_text1 = "Let's make a GIF"
text_text2 = "Select a File"


class VideoToGif:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("700x300+0+0")
        self.window.resizable(0, 0)
        self.window.title("CLARSEN: Video To Gif")

        self.frame = self.create_frame()
        self.text = self.create_text()
        self.button = self.create_button()

    def create_frame(self):
        main_frame = ctk.CTkFrame(
            self.window, width=690, height=290, corner_radius=10, fg_color=bg_fg_color)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_text(self):
        text1 = tk.Label(self.frame, text=text_text1, font=font_style_text1,
                         background=bg_fg_color, foreground=text_color)
        text1.place(relx=0.5, rely=0.5, x=-350, y=-250)

        text2 = tk.Label(self.frame, text=text_text2, font=font_style_text2,
                         background=bg_fg_color, foreground=text_color)
        text2.place(relx=0.5, rely=0.5, x=-120, y=-150)

    def create_button(self):
        button1 = ctk.CTkButton(self.frame, text="Brwose", font=font_style_button1,
                                text_color=text_button1_color, border_width=2, width=10)
        button1.place(relx=0.5, rely=0.5, x=-52, y=-50)

        button2 = ctk.CTkButton(self.frame, text="Create a GIF", font=font_style_button2,
                                text_color=text_button1_color2, border_width=2, width=10)
        button2.place(relx=0.5, rely=0.5, x=-135, y=10)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    video_to_gif = VideoToGif()
    video_to_gif.run()
