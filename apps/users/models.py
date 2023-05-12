from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from apps.common.shared_models import TimeStampedModel


class AppUserManager(BaseUserManager):
    # date_of_birth, password=None):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            # date_of_birth=date_of_birth,
            # date_of_birth=NULL,
        )
        user.username = email
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):  # date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
                                password=password,
                                # date_of_birth=date_of_birth
                                # date_of_birth=NULL
                                )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(TimeStampedModel, AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=128, unique=True, db_index=True)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []