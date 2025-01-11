from typing import Any, Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


def register_user(client: APIClient, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Helper function to register a user and return the response"""
    url = reverse("users:register")
    return client.post(url, payload, format="json")


def verify_email(client: APIClient, token: str) -> Dict[str, Any]:
    """Helper function to verify email with token"""
    url = reverse("users:verify-email", kwargs={"token": token})
    return client.get(url, formate="json")
