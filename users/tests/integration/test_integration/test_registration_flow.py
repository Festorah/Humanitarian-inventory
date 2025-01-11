from unittest.mock import patch

import pytest
from django.urls import reverse
from rest_framework import status

from users.tests.utils.constants import TEST_DATA
from users.tests.utils.helpers import register_user


@pytest.mark.django_db
class TestRegistrationFlow:
    @patch("users.tasks.send_email_verification_mail.delay")
    def test_successful_registration(self, mock_send_email, api_client):
        """Test complete registration flow"""
        response = register_user(api_client, TEST_DATA["VALID_REGISTRATION"])
        assert response.status_code == status.HTTP_201_CREATED
        assert "email" in response.data
        # Verify the email task was called
        mock_send_email.assert_called_once()

    def test_duplicate_email_registration(self, api_client, user_factory):
        """Test registratio with existing email"""
        existing_user = user_factory.create()
        payload = {**TEST_DATA["VALID_REGISTRATION"], "email": existing_user.email}
        response = register_user(api_client, payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
