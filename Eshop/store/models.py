
# products/models.py

from django.db import models
from django.contrib.auth.models import User
class Item(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='item_images/',blank=True,null=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return self.name

class cartItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey('Item',on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    @property
    def total_price(self):
        return self.item.price* self.quantity
# Create your models here.
class PaymentDetail(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    product_name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=0)
    
    payment_id=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}-{self.product_name}-{self.price}" 