from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=100, unique=TRUE)
    slug = models.SlugField(max_length=100, unique=TRUE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="support_posts")
    updated_on = models.DateTimeField(auto_now=TRUE)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=TRUE)
    created_on = models.DateTimeField(auto_now_add=TRUE)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='support_likes', blank=TRUE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
