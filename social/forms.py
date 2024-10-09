from django.forms import Textarea
from django import forms
from .models import Post






class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
        widgets = {
            'body': Textarea(attrs={
                'placeholder': "Share you thoughts!",
                'rows': 2,
                }),
        }
        labels = {
            'body':"",
        }
        