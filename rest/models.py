from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Categories'


class Offer(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
