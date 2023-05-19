from moviepy.editor import VideoFileClip

clip = VideoFileClip("video/3.mp4")
clip.write_gif("mygif.gif")