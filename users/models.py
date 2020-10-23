from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, default=' ', null=True, blank=True)
    employee_cell_phone = models.CharField (max_length=50, default=' ', null=True, blank=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)
