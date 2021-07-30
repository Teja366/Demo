from django.db import models
class Product(models.Model):
    product_img = models.CharField(max_length = 10000)
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    product_mnf = models.CharField(max_length=200)

    class Meta:
        db_table="product_details"
# Create your models here.
