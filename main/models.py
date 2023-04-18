from django.db import models
from django.contrib.auth.models import User


class Music(models.Model):
    file = models.FileField(upload_to='music/',null=False)
    title = models.CharField(max_length=200,null=False)    
    content = models.TextField(max_length=500,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name  ='Track'
        verbose_name_plural = 'Tracks'

    def __str__(self):
        return self.title

class Like(models.Model):
    track = models.ForeignKey(Music,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return self.user.username