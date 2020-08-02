from django.shortcuts import render

# Create your views here.
from .models import Video
from rest_framework import viewsets
from .serializers import VideoSerializer
from rest_framework import filters


# Create your views here.
class VideoViewset(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_fields = ('duration',)
    ordering =('duration',)
