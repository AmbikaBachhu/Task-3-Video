from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    video_file = serializers.FileField(use_url=True)

    class Meta:
        model = Video
        fields = ['id','title','duration','video_file']
