from django.db import models

# Create your models here.
class usermodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.ImageField(default=0)
    password = models.CharField(max_length=20 , default='')

    def __str__(self):
        return self.name