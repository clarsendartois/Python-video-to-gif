from moviepy.editor import VideoFileClip
clip = VideoFileClip("./video/3.mp4")
clip = clip.subclip(0, 5)
clip.write_gif("./Output/test.gif", fps=10)