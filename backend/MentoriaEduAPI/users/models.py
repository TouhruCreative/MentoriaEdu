from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(
            email,
            password,
            **extra_fields,
        )


class User(AbstractUser):
    username = None

    ROLE_CHOICES = (
        ("moderator", "Moderator"),
        ("student", "Student"),
    )

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student",
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set', # Уникальное имя
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set', # Уникальное имя
        blank=True,
    )
    def __str__(self):
        return self.email

# 4Xmas
# class Profile(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         related_name="profile",
#     )

#     avatar = models.ImageField(
#         upload_to="avatars/",
#         blank=True,
#         null=True,
#     )

#     phone = models.CharField(
#         max_length=20,
#         unique=True,
#         blank=True,
#         null=True,
#     )

#     def __str__(self):
#         return f"Profile of {self.user.email}"