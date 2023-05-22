from moviepy.editor import VideoFileClip
clip = VideoFileClip("./video/1.mp4")
# clip = clip.subclip(0, 10)
clip.write_gif("./Output/test1.gif", fps=10)
# gif = VideoFileClip("test5.gif")