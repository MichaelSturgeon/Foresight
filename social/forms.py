# Imported Files and Packages
from django.forms import Textarea
from django import forms
from .models import Post, Profile

# Post Form
class PostForm(forms.ModelForm):
    """
    Posts an instance of Post Form to the database :model:`social.Post`.
    """
    class Meta:
        model = Post
        fields = ('body', )
        widgets = {
            'body': Textarea(attrs={
                'placeholder': "Share you thoughts!",
                'rows': 2,
                'style': 'overflow: hidden'
                }),
        }
        labels = {
            'body':"",
        }

# Profile Image Form
class ProfileImageForm(forms.ModelForm):
    """
    Submits an instance of Profile Image Form to the database :model:`social.Profile`.
    """
    profile_image = forms.ImageField(label='Profile Picture')

    class Meta:
        model = Profile
        fields = ('profile_image', )
        