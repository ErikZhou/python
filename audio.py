from moviepy.editor import AudioFileClip
import sys

#wget https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4
def usage():
    print('python audio.py video_filename')


usage()

video_filename = sys.argv[1]

my_audio_clip = AudioFileClip(video_filename)
my_audio_clip.write_audiofile(video_filename[:-3] + "wav")

