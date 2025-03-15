from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

class Technologies(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    
class Project(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField()
    category = models.ManyToManyField(Category)
    technologies = models.ManyToManyField(Technologies)
    url = models.URLField(null=True)
    github_url = models.URLField()
    complete_date = models.DateTimeField(null=True)
    unggulan = models.BooleanField()

class ImageProject(TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    imag = models.ImageField()
    caption = models.TextField()

class Publication(TimeStampedModel):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    journal = models.CharField(max_length=255,null=True)
    publication_date = models.DateTimeField()
    abstract = models.TextField()
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField()
    url = models.URLField(null=True)
    doi = models.CharField(max_length=255, null=True)
    pdf_file = models.FileField(null=True)