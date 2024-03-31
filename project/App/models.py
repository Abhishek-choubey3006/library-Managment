from django.db import models

class studentDetails(models.Model):
    name = models.CharField(max_length = 100)
    University = models.CharField(max_length = 100)
    branch = models.CharField(max_length = 100)
    session = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    Password = models.CharField(max_length = 20)


