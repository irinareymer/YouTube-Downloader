from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from downloader import utils


@api_view()
def youtube_download(request):
    url = request.query_params.get('url', None)
    file_type = request.query_params.get('type', None)
    data = utils.YoutubeData(url)
    title = data.video_title()
    duration = data.video_duration()
    link = None
    if file_type == 'video':
        link = data.video_downloader()
    elif file_type == 'audio':
        link = data.audio_downloader()
    return Response({"title": title, "duration": duration, "link": link}, status=status.HTTP_200_OK)
