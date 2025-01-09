from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models.object_event_tracker import ObjectEventTracker
from users.models.uuid_primary_key import UUIDPrimaryKey


class Order(UUIDPrimaryKey, ObjectEventTracker):
    class Status(models.TextChoices):
        PENDING = "PENDING", _("Pending")
        DISPATCHED = "DISPATCHED", _("Dispatched")
        DELIVERED = "DELIVERED", _("Delivered")
        CANCELLED = "CANCELLED", _("Cancelled")

    order_number = models.CharField(max_length=50, unique=True)
    items = models.ManyToManyField(
        "inventory.Item", through="OrderItem", related_name="orders"
    )
    region = models.CharField(max_length=255, help_text="Destination region.")
    status = models.CharField(
        max_length=255, choices=Status.choices, default=Status.PENDING
    )

    class Meta:
        indexes = [
            models.Index(fields=["order_number"]),
            models.Index(fields=["region"]),
        ]

    def __str__(self):
        return f"Order {self.order_number} - {self.get_status_display()}"
