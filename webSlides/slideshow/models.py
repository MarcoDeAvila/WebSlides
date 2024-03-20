from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Slides(models.Model):
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=100)
    content = models.TextField(null=False, default="")
    date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
