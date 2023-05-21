# Import everything needed to edit video clips
from moviepy.editor import *
  
   
# loading video dsa gfg intro video
clip = VideoFileClip("./Tuto/1.mp4")
  
  
# getting only first 3 seconds
clip = clip.subclip(0, 5)
  
# saving video clip as gif
clip.write_gif("gfg_gif.gif")
  
# loading  gif
gif = VideoFileClip("gfg_gif.gif")
  
# showing gif
gif.ipython_display()