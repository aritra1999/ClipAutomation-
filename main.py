import os 
import json 
from moviepy.editor import * 

def get_time(interval):
    interval = interval.split(' - ')
    
    return (int(interval[0].split(':')[0]),int(interval[0].split(':')[1])), (int(interval[1].split(':')[0]),int(interval[1].split(':')[1]))


if __name__=="__main__":
    
    with open('data.json') as f:
        clips = json.load(f)       
        
    video_count = 0;
    for clip in clips:
        print("Processing: ", clip)
        print("\nIntervals:")
        
        clip_count = 0
        moviepy_video = VideoFileClip(str("Data/" + clip))
        

        for interval in clips[clip]: 
            start_time, end_time = get_time(interval)
            print("Clip: ", clip_count, "Start: ", start_time, "\tEnd: ", end_time)
            
            clip1 = moviepy_video.subclip(start_time, end_time)
            clip1.write_videofile('result/render_' + str(video_count) + "_" + str(clip_count) + '.mp4', codec='libx264')
            clip_count += 1

        video_count += 1  
        print("Finished Processing!\n\n")
    