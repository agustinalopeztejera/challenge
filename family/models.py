from django.db import models

class Family_members(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    hobbies = models.CharField(max_length=60)
    birthday = models.DateField()
