from django.db import models
from apps.blogs.models import Blog


class Comment(models.Model):
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.blog.id