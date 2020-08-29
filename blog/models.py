from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    featuredImage = models.ImageField(upload_to = 'blog/image')
    auther = models.ForeignKey(User, on_delete= models.CASCADE)
    created_ts = models.DateField(auto_now=True)
    updated_ts = models.DateField(null=True) 

    def __str__(self):
        return self.title


# About Blog
class About(models.Model):
    site_title = models.CharField(max_length = 100)
    site_description = models.TextField()
    meta_tags = models.CharField(max_length = 500)
    created_ts = models.DateField()
    updated_ts = models.DateField(null=True)

    def __str__(self):
        return self.site_title