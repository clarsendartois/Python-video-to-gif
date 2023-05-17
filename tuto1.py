from moviepy.editor import VideoFileClip
clip = VideoFileClip("video/3.mp4")
clip.write_gif("Output/Output.gif", fps=10)