from django.db import models

# Create your models here.
class Education(models.Model):
    course=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)
    institute=models.CharField(max_length=50)
    yop=models.IntegerField()
    percentage=models.FloatField()

class Projects(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics')
    link=models.TextField()
    desc=models.TextField()

class Contacts(models.Model):
    app=models.CharField(max_length=50)
    imagec=models.ImageField(upload_to='pics')
    linkc=models.TextField()

class Techskills(models.Model):
    skill=models.CharField(max_length=50)
    

class Softskills(models.Model):
    skill=models.CharField(max_length=50)

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    msg=models.TextField()
