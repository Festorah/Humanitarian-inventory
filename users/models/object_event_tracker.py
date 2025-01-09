from django.db import models
from django.utils.translation import gettext_lazy as _


class ObjectEventTracker(models.Model):
    """Abstract class to track the history of events and changes related to a model object."""

    created_at = models.DateTimeField(
        verbose_name=_("creation date"),
        editable=False,
        auto_now_add=True,
    )
    created_by = models.UUIDField(
        verbose_name=_("created by"),
        editable=False,
        null=True,
        help_text=_("the Id of the muchmore account user who added this object"),
    )
    last_modified_at = models.DateTimeField(
        verbose_name=_("last modified date"),
        editable=False,
        auto_now=True,
    )
    last_modified_by = models.UUIDField(
        verbose_name=_("last modified by"),
        null=True,
        editable=False,
        help_text=_(
            "the id of the muchmore account user who last modified this object"
        ),
    )

    class Meta:
        abstract = True
