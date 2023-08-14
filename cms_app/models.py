from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def likes_count(self):
        return self.like_set.count()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
