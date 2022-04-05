from django.db import models

# Create your models here.

class signup(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Email = models.EmailField()
    
    def __str__(self):
        return self.FirstName + ' ' + self.LastName


class signin(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    
    def __str__(self):
        return self.FirstName + ' ' + self.LastName