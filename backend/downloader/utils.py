import youtube_dl


class YoutubeData:

    def __init__(self, url):
        with youtube_dl.YoutubeDL() as ydl:
            self.data = ydl.extract_info(url, download=False)

    def video_downloader(self):
        video_link = [f['url'] for f in self.data['formats'] if f['acodec'] != 'none' and f['vcodec'] != 'none']
        return video_link[0]

    def audio_downloader(self):
        audio_link = [f['url'] for f in self.data['formats'] if f['acodec'] != 'none' and f['vcodec'] == 'none']
        return audio_link[0]

    def video_title(self):
        title = self.data['title']
        return title

    def video_duration(self):
        time = self.data['duration']
        hours = (time - (time % 3600)) / 3600
        minutes_and_seconds = (time - hours * 3600)
        minutes = (minutes_and_seconds - (minutes_and_seconds % 60)) / 60
        seconds = minutes_and_seconds - minutes * 60
        duration = f'{int(hours)}:{int(minutes)}:{int(seconds)}'
        return duration
