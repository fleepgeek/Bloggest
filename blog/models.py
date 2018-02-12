from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    creator = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_by_category', args=[self.name])


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="Slug will be automatically generated from the post's title")
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


