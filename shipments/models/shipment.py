from django.db import models
from django.utils.translation import gettext_lazy as _

from orders.models.order import Order
from users.models import ObjectEventTracker, UUIDPrimaryKey


class Shipment(UUIDPrimaryKey, ObjectEventTracker):
    """A shipment of items."""

    class Status(models.TextChoices):
        IN_TRANSIT = "IN_TRANSIT", _("In Transit")
        DELIVERED = "DELIVERED", _("Delivered")
        DELAYED = "DELAYED", _("Delayed")
        CANCELLED = "CANCELLED", _("Cancelled")

    shipment_number = models.CharField(max_length=50, unique=True)
    orders = models.ManyToManyField(Order, related_name="shipments")
    route = models.TextField(help_text="Description of the shipment route.")
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.IN_TRANSIT
    )
    departure_date = models.DateTimeField(verbose_name=_("departure date"))
    arrival_date = models.DateTimeField(
        verbose_name=_("arrival date"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("shipment")
        verbose_name_plural = _("shipments")
        ordering = ("-created_at",)

        indexes = [
            models.Index(fields=["shipment_number"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return f"Shipment {self.shipment_number} - {self.get_status_display()}"
