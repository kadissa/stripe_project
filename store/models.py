"""Django Stripe Orders"""

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE,
                              related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)

    @property
    def items_price(self):
        return self.item.price * self.quantity

    def __str__(self):
        return (f"{self.quantity} x {self.item.name} x {self.item.price} = "
                f"{self.item.price * self.quantity}")


class Order(models.Model):
    items = models.ManyToManyField(Item, through=OrderItem)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(order_item.items_price for order_item in
                   self.order_items.all())

    def __str__(self):
        return f"Order #{self.id}"
