import pytube

yt = YouTube('https://www.youtube.com/watch?v=wIft-t-MQuE&list=PLwGoz2ybZuMT0WgPXPKvrxX2cx-u8WAOX&ab_channel=TaylorSwiftVEVO')
stream = yt.streams.get_by_itag(135)
stream.download()
