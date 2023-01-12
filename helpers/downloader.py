# Description: Downloads a video from a given url
from pytube import YouTube


class VideoDownloader:
    """Downloads a video from a given url"""

    def __init__(self, url, output_path="/User/bashir/Projects/ytd-bot/input-videos"):
        self.url = url
        self.output_path = output_path
        self.yt = YouTube(self.url)

    def download(self):
        # Get the video

        # Get the first stream
        video = (
            self.yt.streams.filter(progressive=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
        )

        # Set the output path
        video.download(output_path=self.output_path)

        print("Video downloaded")

    def vid_title(self):
        return self.yt.streams[0].title
