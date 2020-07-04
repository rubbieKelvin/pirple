from django.db import models

# Create your models here.
class User(models.Model):

    id = models.AutoField(primary_key=True)

    firstname = models.CharField(max_length=20)
    lastname  = models.CharField(max_length=20)
    email     = models.EmailField()
    avatar    = models.ImageField(upload_to='uploads/avatar/%Y/%m/%d/', default=models.NOT_PROVIDED)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Student(User):
    # role = "S"
    pass


class Teacher(User):
    about = models.TextField(max_length=250)


class ClassRoom(models.Model):
    
    id = models.AutoField(primary_key=True)
    
    name        = models.CharField(max_length=20)
    description = models.TextField(default="")
    subject     = models.CharField(max_length=80)
    teachers    = models.ManyToManyField("User", related_name="classrooms")

    def __str__(self):
        return f"{self.name}-{self.id}" 