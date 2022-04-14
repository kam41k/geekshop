from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    activation_key = models.CharField(max_length=128, null=True, blank=True)
    activation_key_expires = models.DateTimeField(null=True, default=(now() +
                                                           timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False

        else:
            return True

    def self_delete(self):
        self.is_active = False
        self.save()
