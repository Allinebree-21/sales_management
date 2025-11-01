# Create your models here.
from django.db import models


class Sale(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # 👈 new field for profit
    date = models.DateField()

    def total_amount(self):
        return self.price * self.quantity

    def profit(self):
        return (self.price - self.cost_price) * self.quantity

    def __str__(self):
        return f"{self.item_name} - {self.quantity} units"