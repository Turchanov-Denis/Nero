from pytube import Playlist

# yt = YouTube(
#     "https://www.youtube.com/watch?v=-mb-3AkZWzE&list=PLHxUjmov4Un9CZP8sDxx4FbXaxxpO3IqE&ab_channel=CHMusicChannel")
link = "https://www.youtube.com/watch?v=RZsL4D4DXNY&list=PLkb7MHt0xUF2WF6UeLUNTRh7YnlqDP-Xg"
pl = Playlist(link)
i = pl.length
print(f"length: {i} ! Mark: notice, what video in playlist can be hide")


def app(i):
    try:
        for yt in pl.videos:
            print(f" CurrentID : {i} - - - Playlist obj: {yt}")
            yt.streams.get_by_itag(22).download(
                r"C:\Users\turch\Desktop\MyPytubeTest\substance_subru")
            i -= 1
            if i == 0:
                return 0
        # print("out")
    except:
        print("Error -- > Retry this dowload")
        app(i)


while i:
    i = app(i)
    print(i)
print("realize!")
# getByStream = yt.streams.get_by_itag(251)
# getByStream.download(r"C:\Users\turch\Desktop\ReactProject\TestReactApp\music\fate")
