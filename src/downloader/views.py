from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from downloader import utils


@api_view()
def youtube_download(request):
    url = request.query_params.get('url', None)
    video_link = utils.video_downloader(url)
    audio_link = utils.audio_downloader(url)
    return Response(status=status.HTTP_200_OK)
