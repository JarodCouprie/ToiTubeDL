from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

ys = yt.streams.get_by_itag("251")
ys.download("Downloads")
print("Download completed!!")