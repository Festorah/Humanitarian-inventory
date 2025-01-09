from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .object_event_tracker import ObjectEventTracker
from .uuid_primary_key import UUIDPrimaryKey


class UserManager(BaseUserManager):
    """
    User account manager for a user model. The user's email address will be used in place of the username
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the supplied email and password
        """
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password or None)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        user: User = self._create_user(email, password, **extra_fields)

        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        user: User = self._create_user(email, password, **extra_fields)

        return user


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

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ("-date_joined",)
        indexes = (
            models.Index(fields=["email"]),
            models.Index(fields=["date_joined"]),
        )

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"

    def get_role_display(self):
        return self.get_role_display()
