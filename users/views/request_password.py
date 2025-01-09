from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.tasks import send_reset_password_link_mail

User = get_user_model()


class RequestPasswordView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get("email")

        try:
            user = User.objects.get(email=email)
            token = jwt.encode(
                {
                    "user_id": str(user.id),
                    "exp": datetime.utcnow() + timedelta(hours=24),
                },
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            send_reset_password_link_mail.delay(user, token)

            return Response(
                {"message": "Password reset link sent to your email."},
                status=status.HTTP_200_OK,
            )
        except User.DoesNotExist:
            return Response(
                {"error": "User with this email does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
