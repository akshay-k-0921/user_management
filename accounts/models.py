from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=150, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True
    )

    mobile_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username
