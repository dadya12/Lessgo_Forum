from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Avatar')
