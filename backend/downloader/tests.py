from rest_framework import status
from rest_framework.test import APIClient
from django.test import SimpleTestCase


class DownloaderTestCase(SimpleTestCase):

    def setUp(self):
        self.client = APIClient()

    def test_success_youtube_download(self):
        response = self.client.get('/download/youtube/',
                                   **{'QUERY_STRING': 'url=https://www.youtube.com/watch?v=dQw4w9WgXcQ&type=video'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data.get('link'))
        self.assertEqual(response.data.get('title'), 'Rick Astley - Never Gonna Give You Up (Official Music Video)')
        self.assertEqual(response.data.get('duration'), '0:3:32')

    def test_no_url_youtube_download(self):
        response = self.client.get('/download/youtube/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_type_youtube_download(self):
        response = self.client.get('/download/youtube/',
                                   **{'QUERY_STRING': 'url=https://www.youtube.com/watch?v=dQw4w9WgXcQ'})
        self.assertIsNone(response.data.get('link'))
