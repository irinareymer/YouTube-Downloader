from django.urls import path

from . import views

urlpatterns = [
    path('youtube/', views.youtube_download),
]
