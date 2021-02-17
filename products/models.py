from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200) #data type character
    price = models.IntegerField()
    image_url = models.URLField(max_length=1000)

    def __str__(self):
        return self.name