from datetime import datetime, timedelta

from celery import shared_task
from django.conf import settings

from users.models.email_verification import EmailVerificationToken
from users.services.email_service import EmailService


@shared_task
def send_email_verification_mail(user_email, token):

    context = {
        "user": user_email,
        "verification_link": f"{settings.FRONTEND_URL}/verify-email/{token}",
    }

    email_service = EmailService(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_email=user_email,
        to_name=user_email,
    )
    email_service.send_email(
        subject="Verify your email address",
        template_name="users/email_verification.html",
        context=context,
    )


@shared_task
def send_reset_password_link_mail(user, token):
    context = {
        "user": user,
        "reset_link": f"{settings.FRONTEND_URL}/reset-password/{token}",
    }

    email_service = EmailService(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_email=user.email,
        to_name=user.email,
    )
    email_service.send_email(
        subject="Password reset link",
        template_name="users/password_reset.html",
        context=context,
    )


@shared_task
def send_reset_password_successful_mail(user):
    context = {
        "user": user,
    }

    email_service = EmailService(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_email=user.email,
        to_name=user.email,
    )
    email_service.send_email(
        subject="Password reset link",
        template_name="users/password_reset_success.html",
        context=context,
    )
