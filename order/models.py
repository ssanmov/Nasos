from django.db import models
from users.models import Profile
from product.models import Product


class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True,  related_name="orders")


class Order_Detail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name="order")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="choosed_prod")
    count = models.IntegerField()
    total_price = models.IntegerField()
    def __str__(self):
        return f"{self.order}"
