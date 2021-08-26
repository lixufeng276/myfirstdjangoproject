from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    # maker = models
    # merchant_id = models.ForeignKey()
    