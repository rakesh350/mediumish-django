from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    featuredImage = models.ImageField(upload_to = 'blog/image')
    auther = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title