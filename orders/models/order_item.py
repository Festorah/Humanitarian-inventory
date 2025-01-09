from django.core.validators import MinValueValidator
from django.db import models

from inventory.models import Item
from orders.models.order import Order
from users.models.object_event_tracker import ObjectEventTracker
from users.models.uuid_primary_key import UUIDPrimaryKey


class OrderItem(UUIDPrimaryKey, ObjectEventTracker):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = ("order", "item")

    def __str__(self):
        return f"{self.item.name} * {self.quantity} (Order {self.order.order_number})"
