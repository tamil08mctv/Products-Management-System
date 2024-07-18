from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    price = models.CharField(max_length=20)
    gst = models.CharField(max_length=10)
    image = models.ImageField(upload_to='static/pics')

    def __str__(self):
        return self.name
