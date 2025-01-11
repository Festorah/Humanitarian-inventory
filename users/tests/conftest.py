import pytest
from rest_framework.test import APIClient

from .factories.user_factory import EmailVerificationTokenFactory, UserFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_factory():
    return UserFactory


@pytest.fixture
def token_factory():
    return EmailVerificationTokenFactory


@pytest.fixture
def authenticated_client(api_client, user_factory):
    user = user_factory.create()
    api_client.force_authenticate(user=user)
    return api_client
