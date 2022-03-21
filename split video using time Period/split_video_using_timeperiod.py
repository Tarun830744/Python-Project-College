from moviepy.editor import *
clip = input('Enter Video file path with video name and extension use (/):')
start = int(input('Enter start time : '))
end = int(input('Enter End time : '))
vid = VideoFileClip(clip)
vid = vid.subclip(start,end)
vid.write_videofile('trim'+str(start)+str(end)+('.mp4') ,codec='libx264')
vid.ipython_display(width = 360)