from django.db import models
from django.contrib.auth.models import User


class LoginLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    username = models.CharField(max_length=150)

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    user_agent = models.TextField(
        blank=True,
        null=True,
    )

    login_time = models.DateTimeField(auto_now_add=True)

    success = models.BooleanField(default=False)

    failure_reason = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["-login_time"]

    def __str__(self):
        return f"{self.username} - {self.login_time}"