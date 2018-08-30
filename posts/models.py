from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE)
    editable = models.BooleanField(default=False)

    def __str__(self):
        return self.title