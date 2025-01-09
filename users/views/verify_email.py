from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.utils import verify_email_token


class VerifyEmailView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, token):
        try:
            is_valid = verify_email_token(token)
            if is_valid:
                return Response(
                    {"message": "Email verified successfully."},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"error": "Invalid or expired token."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"error": f"Failed to verify email: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
