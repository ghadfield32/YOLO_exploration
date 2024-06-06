import os
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

def download_video(yt_video_url):
    HOME = os.getcwd()
    video_path = os.path.join(HOME, 'hq_luka.mp4')

    yt = YouTube(yt_video_url)

    print("Available streams:")
    for stream in yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution'):
        print(stream)

    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download(output_path=HOME, filename='hq_luka.mp4')
    print(f"Downloaded video: {video_path}")

    video = VideoFileClip(video_path)
    duration = video.duration

    start_time = 174  # 2 minutes and 54 seconds
    output_path = os.path.join(HOME, 'hq_luka_cut.mp4')

    ffmpeg_extract_subclip(video_path, start_time, duration, targetname=output_path)
    print(f"Cut video saved to: {output_path}")
    return output_path

