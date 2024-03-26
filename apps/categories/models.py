from django.db import models
from apps.blogs.models import Blog



class Categories(models.Model):
    title = models.CharField(max_length=100,)
    blog = models.ManyToManyField(
        Blog,
        related_name='categories'
    )

    def __str__(self):
        return self.blog.id