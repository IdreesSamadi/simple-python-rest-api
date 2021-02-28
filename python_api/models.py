from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


#classes in python should have two spaces between them
class UserProfileManager(BaseUserManager):
  """Manager for user profile"""
  def create_user(self, email, name, password=None):
    """create a new user profile"""
    if not email:     #checking for error
      raise ValueError('user must have an email address') 

    email = self.normalize_email(email)       # making email lower case
    user = self.model(email=email, name=name)

    user.set_password(password)           #hashing the password
    user.save(using=self._db)             #saving to db,  supports for multiple db

    return user

  def create_superuser(self, email, name, password):
    """create super user with given details"""
    user = self.create_user(email, name, password)

    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)

    return user


class UserProfile(AbstractBaseUser, PermissionsMixin): 
  """Database model for users in the system"""
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserProfileManager()

  USERNAME_FIELD = 'email'      #replacing the default django user name field with the email
  REQUIRED_FIELDS = ['name']

  def get_full_name(self):
    """Retrieve full name user"""
    return self.name

  def get_short_name(self):
    """Retrieve short name of user"""
    return self.name

  def __str__(self):
    """return string representation of the user"""
    return self.email