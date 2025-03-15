from django.db import models
from django_extensions.db.models import TimeStampedModel
# Create your models here.

class Category(TimeStampedModel):
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    
class Tag(TimeStampedModel):
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()

class Post(TimeStampedModel):
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    excerpt = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    published_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=255)
    views_count = models.IntegerField()

class ImagePost(TimeStampedModel):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField()
    caption = models.TextField()
    
class Comment(TimeStampedModel):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    aname = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    approved = models.BooleanField()