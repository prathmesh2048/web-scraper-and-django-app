from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, default='', on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    tag = TaggableManager(blank=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(default=timezone.now)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'
