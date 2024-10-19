from django.forms import Textarea
from django import forms
from .models import Post, Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', )
        widgets = {
            'body': Textarea(attrs={
                'placeholder': "Share you thoughts!",
                'rows': 2,
                }),
        }
        labels = {
            'body':"",
        }


class ProfileImageForm(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile Picture')

    class Meta:
        model = Profile
        fields = ('profile_image', )
        