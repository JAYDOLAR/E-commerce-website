from django.db import models

# Create your models here.
class categorymodel(models.Model):
    name = models.CharField(max_length=20)
    catImage = models.ImageField(upload_to="category")

    def __str__(self):
        return self.name

class productmodel(models.Model):
    category = models.ManyToManyField(categorymodel)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.name