from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()  
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})