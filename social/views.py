from django.shortcuts import render
from .models import Post, Profile

# Create your views here.
def home(request):
    posts = Post.objects.all() 
    return render(request, 'social/index.html', {"posts":posts})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'social/profile_list.html', {"profiles":profiles})
