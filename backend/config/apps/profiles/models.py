from django.db import models
from django_extensions.db.models import TimeStampedModel
# Create your models here.

class Profile(TimeStampedModel):
    
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    bio = models.TextField()
    profile_image = models.ImageField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.TextField()
    cv_file = models.FileField()
    github = models.URLField()
    linkedin = models.URLField()
    
class Education(TimeStampedModel):
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    intitution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    description = models.TextField()
    
class Experience(TimeStampedModel):
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    current = models.BooleanField()
    description = models.TextField()

class Skill(TimeStampedModel):
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    level = models.IntegerField()