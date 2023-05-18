from moviepy.editor import VideoFileClip

video_clip = VideoFileClip("1.mp4")
video_clip.write_gif("gif.gif")