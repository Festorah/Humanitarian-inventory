from datetime import timedelta

import factory
from django.utils import timezone

from users.models import EmailVerificationToken, User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: f"user{n}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "testpass123")
    is_active = True
    is_email_verified = False


class EmailVerificationTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmailVerificationToken

    user = factory.SubFactory(UserFactory)
    token = factory.Faker("uuid4")
    expires_at = factory.LazyFunction(lambda: timezone.now() + timedelta(days=7))
