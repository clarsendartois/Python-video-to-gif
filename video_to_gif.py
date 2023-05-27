import tkinter as tk
import tkinter.filedialog as fd
import customtkinter as ctk
from moviepy.editor import VideoFileClip
import os
import cv2 as cv

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

font_style_text1 = ("Bookman Old Style", 60, "bold")
font_style_text2 = ("Bookman Old Style", 30)
font_style_text3 = ("Bookman Old Style", 40)
font_style_text4 = ("Bookman Old Style", 40)
font_style_button1 = ("Bookman Old Style", 25, "bold")
font_style_button2 = ("Bookman Old Style", 40, "bold")
font_style_button3 = ("Bookman Old Style", 20, "bold")

bg_fg_color = "#2b2b2b"
text_color = "#FFFFFF"
text_color3 = "#26a351"
text_color4 = "#26a351"
text_button_color = "#f97583"

text_text1 = "Let's make a GIF"
text_text2 = "Select a video"
text_text3 = "Successful! Video selected"
text_text4 = "Successful! GIF created"


class VideoToGif:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("700x300+0+0")
        self.window.resizable(0, 0)
        self.window.title("CLARSEN: Video To Gif")

        self.frame = self.create_frame()
        self.select_video = self.create_select_video()

    def create_frame(self):
        main_frame = ctk.CTkFrame(
            self.window, width=690, height=290, corner_radius=10, fg_color=bg_fg_color)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_select_video(self):
        text1 = tk.Label(self.frame, text=text_text1, font=font_style_text1,
                         background=bg_fg_color, foreground=text_color)
        text1.place(relx=0.5, rely=0.5, x=-350, y=-250)

        text2 = tk.Label(self.frame, text=text_text2, font=font_style_text2,
                         background=bg_fg_color, foreground=text_color)
        text2.place(relx=0.5, rely=0.5, x=-140, y=-150)

        button1 = ctk.CTkButton(self.frame, text="Brwose", font=font_style_button1,
                                text_color=text_button_color, border_width=2, width=10, command=self.brwose)
        button1.place(relx=0.5, rely=0.5, x=-52, y=-50)

    def brwose(self):
        global filepath
        file = fd.askopenfile(title='select', mode="r", filetypes=[
            ("All Vidio Format", ".mov"),
            ("All Vidio Format", ".flv"),
            ("All Vidio Format", ".avi"),
            ("All Vidio Format", ".mp4"),
        ])
        if file:
            filepath = os.path.abspath(file.name)
            text3 = tk.Label(self.frame, text=text_text3, font=font_style_text3,
                             background=bg_fg_color, foreground=text_color3)
            text3.place(relx=0.5, rely=0.5, x=-330, y=-25)

            button2 = ctk.CTkButton(self.frame, text="Create a GIF", font=font_style_button2,
                                    text_color=text_button_color, border_width=2, width=10, command=self.create_make_gif)
            button2.place(relx=0.5, rely=0.5, x=-135, y=20)

    def create_make_gif(self):
        clip = VideoFileClip(filepath)
        clip.write_gif("./Output/gif.gif", fps=10)

        text4 = tk.Label(self.frame, text=text_text4, font=font_style_text3,
                         background=bg_fg_color, foreground=text_color4)
        text4.place(relx=0.5, rely=0.5, x=-315, y=150)

        button3 = ctk.CTkButton(self.frame, text="Open your GIF", font=font_style_button3,
                                text_color=text_button_color, border_width=2, width=10, command=self.create_open_gif)
        button3.place(relx=0.5, rely=0.5, x=-80, y=110)

    def create_open_gif(self):
        gif = cv.VideoCapture("./Output/gif.gif")
        while True:
            is_true, frame = gif.read()
            frame = cv.resize(frame, (1200, 700))
            cv.imshow("GIF", frame)
            cv.waitKey(100)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    video_to_gif = VideoToGif()
    video_to_gif.run()
