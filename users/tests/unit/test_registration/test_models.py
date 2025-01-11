import pytest
from django.db import IntegrityError

from users.models import User


@pytest.mark.django_db
class TestUserModel:
    def test_create_user(self, user_factory):
        """Test creating a regular user"""
        user = user_factory.create()
        assert isinstance(user, User)
        assert not user.is_staff
        assert user.is_active

    def test_user_email_unique(self, user_factory):
        """Test email uniqueness constraint"""
        user1 = user_factory.create()
        with pytest.raises(IntegrityError):
            user_factory.create(email=user1.email)
