from django.db import models

class company(models.Model):
    name = models.CharField(max_length=30)
    ceo = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class product(models.Model):
    product_name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.product_name