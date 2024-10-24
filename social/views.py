from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post, Profile
from .forms import PostForm, ProfileImageForm

# Index View
def home(request):
    # Paginate post list
    paginator = Paginator(Post.objects.all(), 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    # Post form
    if request.user.is_authenticated:
        if request.method == "POST":            
            post_form = PostForm(data=request.POST)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, ("Your Post Was Successful!"))             
                return redirect('home')
                
        post_form = PostForm()
        return render(request, 'social/index.html', {"posts":posts,"post_form":post_form,})

    else:
        messages.info(request, ("You Must Be Logged In To Join The Conversation! Click The Link Above To Login, Or Sign-up For An Account Today!"))
        post_form = PostForm()
        return render(request, 'social/index.html', {"posts":posts,"post_form":post_form,})



# Edit Post Veiw    
def edit_post(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)        
        if request.user.username == post.user.username:

            post_form = PostForm(request.POST or None, instance=post) 

            if request.method == "POST":
                if post_form.is_valid():
                    post = post_form.save(commit=False)
                    post.user = request.user
                    post.save()
                    messages.success(request, ("Your Post Has Been Successfully Updated!"))
                    return redirect('home')
            else:
                return render(request, "social/edit_post.html", {'post_form':post_form, 'post':post})
        else:
            messages.error(request, ("This I'snt Your Post To Edit!"))
            return redirect('home')

    else:
        messages.info(request, ("You Must Be Logged In To Complete This Action!"))
        return redirect('home')
        

# Delete Post Veiw    
def delete_post(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)
        if request.user.username == post.user.username:
            
            post.delete()
            messages.success(request, ("Your Post Was Successfully Deleted!"))
            return redirect(request.META.get("HTTP_REFERER"))

        else:
            messages.error(request, ("This I'snt Your Post To Delete!"))
            return redirect('home')
    else:
        messages.info(request, ("You Must Be Logged In To Complete This Action!"))
        return redirect(request.META.get("HTTP_REFERER"))



# Profile List View
def profile_list(request):
    if request.user.is_authenticated:

        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'social/profile_list.html', {"profiles":profiles})

    else:
        messages.info(request, ("You Must Be Logged In To View This Content!")) 
        return redirect('home')


# Profile Page View
def profile_page(request, pk):
    if request.user.is_authenticated:
        profile_posts = Post.objects.filter(user_id=pk).order_by("-created_on")
        profile_page = Profile.objects.get(user_id=pk)
        profile_user = Profile.objects.get(user__id=request.user.id)
        
        # Upload Profile Image Form
        profile_image_form = ProfileImageForm(request.POST or None, request.FILES or None, instance=profile_user)
        if profile_image_form.is_valid():
            profile_image_form.save()
            messages.success(request, ("Your Profile Image Was Successfully Updated!"))
            return redirect(request.META.get("HTTP_REFERER"))
            

        return render(request, 'social/profile_page.html', {
            "profile_page":profile_page,
            "profile_posts":profile_posts,
            "profile_image_form":profile_image_form,
        })

    else:
        
        return redirect('home')


# Like Post View
def post_like(request, pk):
	if request.user.is_authenticated:
		post = get_object_or_404(Post, id=pk)
        
		if post.likes.filter(id=request.user.id):
			post.likes.remove(request.user)
		else:
			post.likes.add(request.user)
		
		return redirect(request.META.get("HTTP_REFERER"))


	else:
		messages.info(request, ("You Must Be Logged In To Like A Post!"))
		return redirect('home')


# Unfollow Profile View
def unfollow(request, pk):
    if request.user.is_authenticated:
        profile_page = Profile.objects.get(user_id=pk)
        request.user.profile.follows.remove(profile_page)
        request.user.profile.save()
        messages.info(request, (f"You Have Unfollowed {profile_page.user.username}"))
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.info(request, ("You Must Be Logged In To Unfollow Other Users!"))
        return redirect('home')


# Follow Profile View
def follow(request, pk):
    if request.user.is_authenticated:
        profile_page = Profile.objects.get(user_id=pk)
        request.user.profile.follows.add(profile_page)
        request.user.profile.save()
        messages.success(request, (f"You Have Successfully Followed {profile_page.user.username}"))
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.info(request, ("You Must Be Logged In To Follow Other Users!"))
        return redirect('home')       
