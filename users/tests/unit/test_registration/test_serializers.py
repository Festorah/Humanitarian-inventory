import pytest

from users.serializers import UserRegistrationSerializer
from users.tests.utils.constants import TEST_DATA


@pytest.mark.django_db
class TestUserRegistrationSerializer:
    def test_valid_serializer_data(self):
        """Test serializer with valid data"""
        serializer = UserRegistrationSerializer(data=TEST_DATA["VALID_REGISTRATION"])
        assert serializer.is_valid()

    def test_invalid_password_match(self):
        """Test password mismatch validation"""
        serializer = UserRegistrationSerializer(
            data=TEST_DATA["INVALID_REGISTRATION"]["MISMATCHED_PASSWORDS"]
        )
        assert not serializer.is_valid()
        assert "password" in serializer.errors
