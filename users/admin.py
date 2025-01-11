from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from inventory_management.sites import admin_site
from users.models import EmailVerificationToken, User


@admin.register(User, site=admin_site)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "is_active",
        "is_email_verified",
    )
    list_display_links = ("id",)
    list_filter = ("is_email_verified",)


@admin.register(EmailVerificationToken, site=admin_site)
class EmailVerificationTokenAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "token",
    )
    list_display_links = ("id",)
    list_filter = ("user",)
