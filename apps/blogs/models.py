from django.db import models


class BlogTag(models.Model):
    blog = models.CharField(
        max_length=120,
    )

    def __str__(self):
        return self.id


class Blog(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    tag = models.ManyToManyField(
        BlogTag,
        related_name='tag'
    )

    def __str__(self):
        return self.id


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


class BlogLike(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='like'

    )


