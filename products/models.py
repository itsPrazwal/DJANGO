from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)  # data type character
    price = models.IntegerField()
    image_url = models.URLField(max_length=1000)

    def __str__(self):
        return self.name


class Person(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
