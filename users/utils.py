from datetime import datetime

from rest_framework_simplejwt.tokens import RefreshToken

from users.models.email_verification import EmailVerificationToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


def verify_email_token(token):
    try:
        verification_token = EmailVerificationToken.objects.get(
            token=token, expires_at__gt=datetime.now()
        )
        user = verification_token.user
        user.is_email_verified = True
        user.save(update_fields=["is_email_verified"])
        verification_token.delete()
        return True
    except EmailVerificationToken.DoesNotExist:
        return False
