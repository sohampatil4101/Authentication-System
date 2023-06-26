from django.db import models

# Create your models here.

class Doctor(models.Model):
    username = models.TextField(max_length = 20)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    address = models.TextField()
    image = models.FileField(upload_to='images/', default = 0)

    def __str__(self):
        return self.username


class Patient(models.Model):
    username = models.TextField(max_length = 20)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    address = models.TextField()
    image = models.FileField(upload_to='images/', default = 0)

    def __str__(self):
        return self.username


category_choice = (
    ("Mental Health", "Mental Health"),
    ("Heart Disease", "Heart Disease"),
    ("Covid19", "Covid19"),
    ("Immunization" , "Immunization "),
)


class Createblog(models.Model):
    username = models.TextField()
    title = models.TextField()
    image = models.FileField(upload_to='images/', default = 0)
    category = models.TextField(choices = category_choice, default = 'Mental Health')
    summary = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title + " " + self.category

class Draftblog(models.Model):
    username = models.TextField()
    title = models.TextField()
    image = models.FileField(upload_to='images/', default = 0)
    category = models.TextField(choices = category_choice, default = 'Mental Health')
    summary = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title + " " + self.category