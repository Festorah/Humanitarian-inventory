from django.core.validators import MinValueValidator
from django.db import models

from users.models.object_event_tracker import ObjectEventTracker
from users.models.uuid_primary_key import UUIDPrimaryKey


class Item(UUIDPrimaryKey, ObjectEventTracker):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    location = models.CharField(
        max_length=255, help_text="Storage location of the item."
    )
    expiry_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["expiry_date"]),
        ]

    def __str__(self):
        return f"{self.name} (Qty: {self.quantity})"
