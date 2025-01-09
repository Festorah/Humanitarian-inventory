import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class PasswordResetSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "Passwords fields didn't match."}
            )

        try:
            # Verify the token
            payload = jwt.decode(
                attrs["token"], settings.SECRET_KEY, algorithms=["HS256"]
            )
            user = User.objects.get(id=payload["user_id"])
            attrs["user"] = user
        except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
            raise serializers.ValidationError(
                {"token": "Invalid or expired reset token."}
            )

        # Validate password
        validate_password(attrs["new_password"])
        return attrs
