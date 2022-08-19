from django.db import models


class Category(models.Model):
    name = models.CharField(blank=False, null=False,max_length=150)
    image = models.ImageField(blank=True, null=True)
    def __str__(self):
        return f"{self.name}"


class Subcategory(models.Model):
    name = models.CharField(blank=False, null=False, max_length=150)
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="kategory")
    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(blank=False, null=False, max_length=150)
    image = models.ImageField(blank=True, null=True)
    description = models.CharField(blank=True, null=True, max_length=500)
    kvt = models.FloatField(blank=True,null=True)
    litre_min = models.FloatField(blank=True,null=True)
    climb = models.FloatField(blank=True,null=True)
    price = models.IntegerField(blank=False, null=False)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, related_name="product")
    def __str__(self):
        return f"{self.name}"





