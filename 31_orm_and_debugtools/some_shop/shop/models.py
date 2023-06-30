from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True,)
    description = models.CharField(max_length=200,)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product<{self.pk}, {self.name!r}>"
