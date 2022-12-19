from .models import Post, Thread
from django import forms


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('title', 'slug', 'author', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
