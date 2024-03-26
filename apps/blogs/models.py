from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )


class BlogImage(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE,
        related_name='blog_images'
    )
    image = models.ImageField(
        upload_to='blogs/'
    )

    def __str__(self):
        return self.blog.title
