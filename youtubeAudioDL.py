from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

#print(yt.streams.filter(file_extension="mp4",only_audio=True))


#itag only video mp4 1080p = 137
#itag only audio mp4 128kbps = 140
ys = yt.streams.get_by_itag("140")
ys.download("Downloads")
print("Download completed!!")