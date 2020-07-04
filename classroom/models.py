from django.db import models

# Create your models here.
class User(models.Model):
    
    id = models.AutoField(primary_key=True)

    firstname = models.CharField(max_length=20)
    lastname  = models.CharField(max_length=20)
    email     = models.EmailField()
    avatar    = models.ImageField(upload_to='uploads/avatar/%Y/%m/%d/', default=models.NOT_PROVIDED)