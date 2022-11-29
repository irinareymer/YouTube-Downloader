from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from downloader import utils


@api_view()
def youtube_download(request):
    url = request.query_params.get('url', None)
    data = utils.YoutubeData(url)
    title = data.video_title()
    duration = data.video_duration()
    video_link = data.video_downloader()
    audio_link = data.audio_downloader()
    return Response(status=status.HTTP_200_OK)
