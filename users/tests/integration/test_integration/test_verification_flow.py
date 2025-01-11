from datetime import timedelta

import pytest
from django.utils import timezone

from users.tests.utils.helpers import verify_email


@pytest.mark.django_db
class TestVerificationFlow:
    def test_successful_verification(self, api_client, user_factory, token_factory):
        """Test successful email verification"""
        user = user_factory.create(is_email_verified=False)
        token = token_factory.create(user=user)
        response = verify_email(api_client, token.token)
        user.refresh_from_db()
        assert response.status_code == 200
        assert user.is_email_verified

    def test_expired_token_verification(self, api_client, user_factory, token_factory):
        """Test email verification with expired token"""
        user = user_factory.create(is_email_verified=False)
        token = token_factory.create(
            user=user, expires_at=timezone.now() - timedelta(days=1)
        )
        token.created_at = timezone.now() - timedelta(days=3)
        response = verify_email(api_client, token.token)

        assert response.status_code == 400
        assert "expired" in response.data["error"].lower()
