from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def youtube_download(request):
    url = request.query_params.get('url', None)
    return Response(status=status.HTTP_200_OK)
