from moviepy.editor import *

clip = (VideoFileClip("video/3.mp4")
        .subclip((1,22.65),(1,23.2))
        .resize(0.3))
clip.write_gif("3a.gif")