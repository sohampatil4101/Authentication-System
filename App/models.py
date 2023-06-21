from django.db import models

# Create your models here.

class Doctor(models.Model):
    username = models.TextField(max_length = 20)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.TextField()
    address = models.TextField()
    pincode = models.TextField()
    image = models.FileField(upload_to='images/', default = 0)

    def __str__(self):
        return self.username


class Patient(models.Model):
    username = models.TextField(max_length = 20)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.TextField()
    address = models.TextField()
    pincode = models.TextField()
    image = models.FileField(upload_to='images/', default = 0)

    def __str__(self):
        return self.username

