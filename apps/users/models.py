from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    date_joined = models.DateTimeField(
        default=timezone.now
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class UserProfile(models.Model):

    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
        ("T", "TransSexual")
    )

    # Required
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=10)
    nickname = models.CharField(max_length=20)
    phonenumber = PhoneNumberField(null=False, blank=False, unique=True)

    # Optional
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=2, choices=GENDER, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=True, null=True)
    
    REQUIRED_FIELDS = ['username', 'nickname', 'email', 'phonenumber']

    def __str__(self):
        return self.nickname
    
    def get_full_name(self):        
        return self.nickname

    def get_short_name(self):
        return self.nickname
    

class Address(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    home_address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    
    def __str__(self):
        return self.home_address