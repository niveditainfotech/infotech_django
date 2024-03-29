from django.db import models

# Create your models here.

class CallReq(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    description=models.TextField(blank=False)

    def __str__(self):
        return self.name
    

class contactMsg(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField(blank=False)

    def __str__(self):
        return self.name
    
class Intermship(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    course=models.CharField(max_length=20)
    duration=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Careers(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    role=models.CharField(max_length=10)
    resume=models.FileField(upload_to="resume/")

    def __str__(self):
        return self.name