from pytube import YouTube, Playlist
import sys
import pathlib
sys.path.append(str(pathlib.Path().resolve()))
# yt = YouTube("https://www.youtube.com/watch?v=buDG1M6ZWSE&ab_channel=OnsaMedia")


# stream = yt.streams.get_by_itag(140)  # 140 audio // 22 720p
# stream.download()

class YtManager:
    def __init__(self, bd):  # bd: Warehouse
        self.bd = bd
        print(id(self.bd), id(bd))

    def dowloadVA(self):
        try:
            yt = YouTube(self.bd.link)
            stream = yt.streams.get_by_itag(self.bd.pytubeTag)
            stream.download()
        except:
            pass

    def dowloadPl(self):
        try:
            p = Playlist(self.bd.link)
            for video in p.videos:
                video.streams.get_by_itag(self.bd.pytubeTag).download()
        except:
            pass


if __name__ == "__main__":
    from app import Warehouse
    yt = YtManager(Warehouse())
