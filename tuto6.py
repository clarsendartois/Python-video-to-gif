from moviepy.editor import *
convert_video_name = VideoFileClip("./video/3.mp4")
convert_video_name.write_gif("./Output/gif.gif")