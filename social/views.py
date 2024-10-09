from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post, Profile

# Index View
def home(request):
    # Paginate post list
    paginator = Paginator(Post.objects.all(), 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)


    return render(request, 'social/index.html', {
        "posts":posts,
    })


# Profile List View
def profile_list(request):
    if request.user.is_authenticated:

        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'social/profile_list.html', {"profiles":profiles})

    else:
        # ONCE CREATAED, REDIRECT USER TO LOGIN PAGE
        return redirect('home')


# profile_page View
def profile_page(request, pk):
    if request.user.is_authenticated:

        profile_posts = Post.objects.filter(user_id=pk).order_by("-created_on")
        profile_page = Profile.objects.get(user_id=pk)

        # Follow/ Unfollow form request
        if request.method == "POST":
            user_profile = request.user.profile
            action = request.POST["follow"]
            if action == "unfollow":
                user_profile.follows.remove(profile_page)
            else:
                user_profile.follows.add(profile_page)
            user_profile.save()


        return render(request, 'social/profile_page.html', {
            "profile_page":profile_page,
            "profile_posts":profile_posts,
        })

    else:
        # ONCE CREATAED, REDIRECT USER TO LOGIN PAGE
        return redirect('home')
