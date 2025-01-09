from django.contrib.auth import get_user_model, login, logout
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers.login import LoginSerializer
from users.serializers.user import UserSerializer
from users.utils import get_tokens_for_user

User = get_user_model()


class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            user = serializer.validated_data["user"]

            # Session-based auth
            if request.data.get("use_session", False):
                login(request, user)
                response_data = {
                    "message": "Successfully logged in",
                    "user": UserSerializer(user).data,
                    "session_based": True,
                }
            else:
                tokens = get_tokens_for_user(user)
                response_data = {
                    "tokens": tokens,
                    "user": UserSerializer(user).data,
                    "session_based": False,
                }

            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
