from rest_framework import status
from rest_framework.test import APITestCase
from user_management.test_utils import create_user, get_authenticated_client


class AccountAPITests(APITestCase):

    def test_user_registration(self):
        response = self.client.post(
            "/api/auth/register/",
            {
                "username": "newuser",
                "email": "newuser@test.com",
                "password": "StrongPass123"
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_and_get_profile(self):
        user = create_user()
        client = get_authenticated_client(user)

        response = client.get("/api/auth/profile/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # ✅ Correct assertion
        self.assertIn("full_name", response.data["data"])

    def test_update_profile(self):
        user = create_user()
        client = get_authenticated_client(user)

        response = client.patch(
            "/api/auth/profile/",
            {"full_name": "Updated Name"},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]["full_name"], "Updated Name")

    def test_reset_password(self):
        user = create_user()
        client = get_authenticated_client(user)

        response = client.post(
            "/api/auth/reset-password/",
            {"new_password": "NewStrongPass123"},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
