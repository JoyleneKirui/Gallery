from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class pics(models.Model):

    
    imgtitle=models.CharField(max_length=100)
    imgdesc=models.CharField(max_length=500)
    image=models.ImageField(upload_to='images/')

