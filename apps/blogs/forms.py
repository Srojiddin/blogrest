from django import forms
from apps.blogs.models import Blog, BlogImage


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title',
            'description'
        )


class BlogImageForm(forms.ModelForm):
    class Meta:
        model = BlogImage
        fields = (

        )