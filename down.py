from pytube import YouTube
import sys
#YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams.first().download()
#yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
#print(yt.streams)
#print(yt.streams.filter(subtype='mp4'))
#yt.streams.filter(progressive=True)
#print(yt.streams.filter(progressive=True).order_by('resolution').desc())

def main():
    url = sys.argv[1]
    print(url)
    path = './videos/1.mp4'
    #YouTube(url).streams.first().download()
    YouTube(url).streams.first().download(path)
    print('Done')


if __name__ == "__main__":
    #usage()    
    main()
