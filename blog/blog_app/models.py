from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.



class User(AbstractUser):
    profile_image = models.FileField(upload_to='profile')



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='user')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    

class Comments(models.Model):
    writer = models.ForeignKey(Post, on_delete=models.RESTRICT, related_name='comment')
    contents = models.TextField()
    date = models.DateField(datetime.now())

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    bio= models.TextField(max_length=400, blank=True)
    profile_img= models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    birth_date= models.DateField(null=True, blank=True)
    location= models.TextField(blank=True, max_length=35)

    def __str__(self):
        return f'{self.user.username} profile'