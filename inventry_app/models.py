from django.db import models
import datetime
from django.utils import timezone

userName = 'admin'


def get_upload_path(instance, filename):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    sku_folder = instance.product.sku.replace('/', '_')
    return f'productImage/{sku_folder}/{timestamp}_{filename}'


def get_upload_path_listedOnline(instance, filename):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    sku_folder = instance.product.sku.replace('/', '_')
    return f'listedOnlineImages/{sku_folder}/{timestamp}_{filename}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    createdBy = models.CharField(
        max_length=100, default=userName, null=True)
    createdBy = models.CharField(max_length=100, default=userName, null=True)
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    modifiedBy = models.CharField(max_length=100, default=userName, null=True)
    modifiedOn = models.DateTimeField(auto_now=True, null=True)
    isActive = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Product1(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    description = models.TextField()
    createdBy = models.CharField(max_length=100, default=userName, null=True)
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    modifiedBy = models.CharField(max_length=100, default=userName, null=True)
    modifiedOn = models.DateTimeField(auto_now=True, null=True)
    isActive = models.IntegerField(default=1)

    def __str__(self):
        return self.sku


class Image1(models.Model):
    product = models.ForeignKey(
        Product1, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path)
    createdBy = models.CharField(max_length=100, default=userName, null=True)
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    modifiedBy = models.CharField(max_length=100, default=userName, null=True)
    modifiedOn = models.DateTimeField(auto_now=True, null=True)
    isActive = models.IntegerField(default=1)

    def __str__(self):
        return self.image.name


class ecommerceSites(models.Model):
    name = models.CharField(max_length=100)
    createdBy = models.CharField(
        max_length=100, default=userName, null=True)
    createdBy = models.CharField(max_length=100, default=userName, null=True)
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    modifiedBy = models.CharField(max_length=100, default=userName, null=True)
    modifiedOn = models.DateTimeField(auto_now=True, null=True)
    isActive = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class listedOnline(models.Model):
    sku = models.ForeignKey(Product1, on_delete=models.CASCADE)
    listedSite = models.ForeignKey(ecommerceSites, on_delete=models.CASCADE)
    productTitle = models.CharField(max_length=100)
    productID = models.CharField(max_length=100)
    listedCategory = models.CharField(max_length=100)
    listedPrice = models.DecimalField(max_digits=10, decimal_places=2)
    buyedPrice = models.DecimalField(max_digits=10, decimal_places=2)
    quantityPerOrder = models.IntegerField()
    lengthBefore = models.DecimalField(max_digits=10, decimal_places=2)
    widthBefore = models.DecimalField(max_digits=10, decimal_places=2)
    heightBefore = models.DecimalField(max_digits=10, decimal_places=2)
    lengthAfter = models.DecimalField(max_digits=10, decimal_places=2)
    widthAfter = models.DecimalField(max_digits=10, decimal_places=2)
    heightAfter = models.DecimalField(max_digits=10, decimal_places=2)
    weightBefore = models.DecimalField(max_digits=10, decimal_places=2)
    weightAfter = models.DecimalField(max_digits=10, decimal_places=2)
    createdBy = models.CharField(max_length=100, default=userName, null=True)
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    modifiedBy = models.CharField(max_length=100, default=userName, null=True)
    modifiedOn = models.DateTimeField(auto_now=True, null=True)
    isActive = models.IntegerField(default=1)

    def __str__(self):
        return self.sku


class listedOnlineImages(models.Model):
    product = models.ForeignKey(
        listedOnline, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path_listedOnline)
    createdBy = models.CharField(max_length=100, default=userName, null=True)
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    modifiedBy = models.CharField(max_length=100, default=userName, null=True)
    modifiedOn = models.DateTimeField(auto_now=True, null=True)
    isActive = models.IntegerField(default=1)

    def __str__(self):
        return self.image.name
