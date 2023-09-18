from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250, verbose_name='Sarlavha')
    summary = models.CharField(max_length=300)
    body = models.TextField()
    at_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
