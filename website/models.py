from django.db import models

class Contact_form(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=100)


