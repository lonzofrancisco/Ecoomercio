from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,PermissionsMixin,UserManager
)


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Se requiere correo electronico.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)        
        user.set_password(password)
        
