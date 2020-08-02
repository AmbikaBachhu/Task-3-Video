from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    duration = models.FloatField()
    video_file = models.FileField(upload_to='upload/videofiles', blank=True, )

    def __str__(self):
        return self.title
