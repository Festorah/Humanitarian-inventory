import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class UUIDPrimaryKey(models.Model):
    id = models.UUIDField(
        verbose_name="id",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text=_("UUID primary key"),
    )

    class Meta:
        abstract = True
