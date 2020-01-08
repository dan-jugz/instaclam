from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Profile, Follow
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    images = Post.objects.all()
    params = {
        'images': images,
    }
    return render(request, 'instagram/index.html', params)   