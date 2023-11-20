from django.db import models

# Create your models here.


class StoreItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    origin = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    amount_sold = models.PositiveIntegerField()

    def __str__(self):
        return self.title
