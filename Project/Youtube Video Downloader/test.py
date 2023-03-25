from pytube import YouTube
vid=YouTube("https://www.youtube.com/watch?v=mpnh1YTT66w")
#print (vid.streams)
hvid=vid.streams.get_highest_resolution()
hvid.download("/Videos")