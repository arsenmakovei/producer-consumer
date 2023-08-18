from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    probation = models.BooleanField(default=False)
    position = models.CharField(max_length=63)


class Order(models.Model):
    task_id = models.CharField(max_length=63)
    name = models.CharField(max_length=63)
    description = models.TextField(max_length=255)
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders"
    )

    def __str__(self) -> str:
        return f"{self.name} {self.task_id}"
