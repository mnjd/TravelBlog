from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # add thumbnail

    # function to show title of articles
    def __str__(self):
        return self.title

    def is_updated(self):
        return self.created_at != self.updated_at
