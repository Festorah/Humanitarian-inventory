from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .object_event_tracker import ObjectEventTracker
from .uuid_primary_key import UUIDPrimaryKey


class User(UUIDPrimaryKey, ObjectEventTracker, AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", _("Admin")
        FIELD_WORKER = "FIELD_WORKER", _(" Field Worker")
        LOGISTICS_MANAGER = "LOGISTICS_MANAGER", _("Logistics Manager")

    email = models.EmailField(_("email address"), unique=True)
    is_email_verified = models.BooleanField(default=False)
    role = models.CharField(
        max_length=20, choices=Role.choices, default=Role.FIELD_WORKER
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    def get_role_display(self):
        return self.get_role_display()
