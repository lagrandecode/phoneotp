from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.db import IntegrityError
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        new_user = self.model(email=email,**extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff as True"))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser should have is_superuser as True"))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser should have is_active as True"))

        return self.create_user(email,password,**extra_fields)


class User(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=12,unique=True)
    otp = models.CharField(max_length=200,null=True,blank=True)
    isVerified = models.BooleanField(default=False)

    USERNAME_FIELD = 'phome_number'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

    def __str__(self):
        return f"<User {self.email}"

class UserInfo(models.Model):
    address = models.CharField(max_length=250)
    desc = models.CharField(max_length=100)