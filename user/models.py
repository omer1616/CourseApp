from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profiller"

    def __str__(self):
        return f"{self.user.username}-{self.phone_number}"

