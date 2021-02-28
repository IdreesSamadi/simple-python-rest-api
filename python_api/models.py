from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin


class UserProfile(AbstractBaseUser, PermissionMixin): 
  """Database model for users in the system"""
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserProfileManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDs = ['name']

  def get_full_name(self):
    """Retrieve full name user"""
    return self.name

  def get_short_name(self):
    """Retrieve short name of user"""
    return self.name

  def __str__(self):
    """return string representation of the user"""
    return self.email