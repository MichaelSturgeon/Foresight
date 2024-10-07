from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post, Profile

# Create your views here.
def home(request):
    # Paginate post list
    paginator = Paginator(Post.objects.all(), 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)


    return render(request, 'social/index.html', {
        "posts":posts,
    })


def profile_list(request):
    if request.user.is_authenticated:

        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'social/profile_list.html', {"profiles":profiles})

    else:
        # ONCE CREATAED, REDIRECT USER TO LOGIN PAGE
        return redirect('home')


def my_profile(request):
    if request.user.is_authenticated:

        return render(request, 'social/my_profile.html', {})

    else:
        # ONCE CREATAED, REDIRECT USER TO LOGIN PAGE
        return redirect('home')
