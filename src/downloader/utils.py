import youtube_dl


def video_downloader(url):
    with youtube_dl.YoutubeDL() as ydl:
        r = ydl.extract_info(url, download=False)
    video_link = [f['url'] for f in r['formats'] if f['acodec'] != 'none' and f['vcodec'] != 'none']
    return video_link[0]
