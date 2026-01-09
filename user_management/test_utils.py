from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import Profile


def create_user(username="testuser"):
    user = User.objects.create_user(
        username=username,
        email=f"{username}@test.com",
        password="test1234"
    )

    Profile.objects.create(
        user=user
    )

    return user


def get_authenticated_client(user):
    client = APIClient()

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    return client

