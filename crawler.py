from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=RzhAS_GnJIc')
stream = yt.streams.get_by_itag(135)
stream.download()
