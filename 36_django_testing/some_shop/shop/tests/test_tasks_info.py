from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from typing import Type
from django.contrib.auth import get_user_model


UserModel: Type[AbstractUser] = get_user_model()


class GetTaskInfoTestCase(TestCase):
    def setUp(self) -> None:
        self.username = "user_testing"
        self.password = "Qwerty123$"
        self.user: AbstractUser = UserModel.objects.create_user(username=self.username, password=self.password)
        # print("Created User:", self.user)
        # self.client.login(username=self.username, password=self.password)

    def test_anon_user_no_access(self):
        # self.client.logout()
        task_id = "21"
        url = reverse("shop:get-order-task", kwargs={"task_id": task_id})
        response = self.client.get(url)
        # self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("site_auth:login") + f"?next={url}")
        print("Response:", response)

    def test_get_task_info_pending(self):
        task_id = "21"
        url = reverse("shop:get-order-task", kwargs={"task_id": task_id})
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(url)
        self.assertJSONEqual(response.content,
                             {"task_id": task_id,
                              "status": "PENDING",
                              "name": None,
                              }
                             )
        print(response.content)
