from unittest.mock import patch

import pytest

from users.tasks import send_email_verification_mail


@pytest.mark.django_db
class TestEmailVerification:
    @patch("users.services.email_service.EmailService.send_email")
    def test_verification_email_sending(
        self, mock_send_email, user_factory, token_factory
    ):
        """Test email verification sending flow"""
        user = user_factory.create()
        token = token_factory.create(user=user)

        send_email_verification_mail(user.email, token.token)

        mock_send_email.assert_called_once()
        call_kwargs = mock_send_email.call_args[1]
        assert "Verify your email" in call_kwargs["subject"]
        assert token.token in call_kwargs["context"]["verification_link"]
