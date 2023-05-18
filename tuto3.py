from moviepy.editor import VideoFileClip

clip = VideoFileClip("Tuto/1.mp4")
clip.write_gif("Output/video2gif.gif")