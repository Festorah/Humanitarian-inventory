import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from .user import User


class EmailVerificationToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        verbose_name = _("email verification token")
        verbose_name_plural = _("email verification tokens")
