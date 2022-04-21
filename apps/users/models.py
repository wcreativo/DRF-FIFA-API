from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from simple_history.models import HistoricalRecords

class UserProfileManager(BaseUserManager):

    def create_user(self, name, email, password=None):

        if not email:
            raise ValueError('El usuario debe tener un email')
        email = self.normalize_email(email)
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self) -> str:
        return self.name
