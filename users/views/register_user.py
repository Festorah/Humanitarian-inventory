from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models.email_verification import EmailVerificationToken
from users.serializers.user import UserRegistrationSerializer
from users.tasks import send_email_verification_mail

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user = User.objects.get(id=user.id)
        token = EmailVerificationToken.objects.create(
            user=user, expires_at=timezone.now() + timedelta(days=7)
        )

        token.save()
        send_email_verification_mail.delay(user_email=user.email, token=token.token)

        return Response(
            {
                "message": "User created successfully. Please check your email to verify your account."
            },
            status=status.HTTP_201_CREATED,
        )
