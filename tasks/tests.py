from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Task
from user_management.test_utils import create_user, get_authenticated_client


class TaskAPITests(APITestCase):

    def setUp(self):
        self.user = create_user()
        self.client = get_authenticated_client(self.user)

    # -------------------------
    # CREATE TASK
    # -------------------------
    def test_create_task(self):
        response = self.client.post(
            "/api/tasks/",
            {
                "title": "Test Task",
                "description": "Task description"
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, "Test Task")

    # -------------------------
    # LIST TASKS (PAGINATED)
    # -------------------------
    def test_list_tasks_paginated(self):
        # Create multiple tasks
        for i in range(7):
            Task.objects.create(
                user=self.user,
                title=f"Task {i}",
                description="Desc"
            )

        response = self.client.get("/api/tasks/?page=1")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # ✅ Correct pagination keys
        self.assertIn("results", response.data)
        self.assertIn("count", response.data)
        self.assertIn("next", response.data)
        self.assertIn("previous", response.data)

        # Validate data
        self.assertTrue(len(response.data["results"]) > 0)
        self.assertEqual(response.data["count"], 7)

    # -------------------------
    # RETRIEVE TASK
    # -------------------------
    def test_retrieve_task(self):
        task = Task.objects.create(
            user=self.user,
            title="My Task",
            description="Desc"
        )

        response = self.client.get(f"/api/tasks/{task.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "My Task")

    # -------------------------
    # UPDATE TASK
    # -------------------------
    def test_update_task(self):
        task = Task.objects.create(
            user=self.user,
            title="Old Title",
            description="Desc"
        )

        response = self.client.patch(
            f"/api/tasks/{task.id}/",
            {"title": "New Title"},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        task.refresh_from_db()
        self.assertEqual(task.title, "New Title")

    # -------------------------
    # DELETE TASK
    # -------------------------
    def test_delete_task(self):
        task = Task.objects.create(
            user=self.user,
            title="Delete Me",
            description="Desc"
        )

        response = self.client.delete(f"/api/tasks/{task.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
