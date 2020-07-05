from django.db import models
from django.contrib.auth.models import User as BaseUser

# Create your models here.
class User(BaseUser):
    avatar    = models.ImageField(upload_to='uploads/avatar/%Y/%m/%d/', default=models.NOT_PROVIDED)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ClassRoom(models.Model):
    
    id = models.AutoField(primary_key=True)
    
    name        = models.CharField(max_length=20)
    description = models.TextField(default="")
    subject     = models.CharField(max_length=80)
    members    = models.ManyToManyField("User", related_name="classrooms")

    def __str__(self):
        return f"{self.name}-{self.id}" 


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(choices=[
        ("T", "teacher"),
        ("S", "student")
    ], max_length=1)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
