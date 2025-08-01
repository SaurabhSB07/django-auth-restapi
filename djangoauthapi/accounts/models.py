from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None,password2=True):
        """
        Creates and saves a User with the given email, name,tc and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        """
        Creates and saves a superuser with the given email, name,tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc
            
        )
        user.is_admin = True
        
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    name=models.CharField(max_length=50)
    tc=models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","tc"]

    def __str__(self):
        return self.email

    
