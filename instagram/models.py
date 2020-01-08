from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return f"/post/{self.id}"