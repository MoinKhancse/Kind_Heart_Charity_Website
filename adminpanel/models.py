from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class slider(models.Model):
    slider_title = models.CharField(max_length=200)
    slider_description = models.CharField(max_length=200)
    slider_image = models.ImageField(upload_to='slider/', blank=True,null=True)
