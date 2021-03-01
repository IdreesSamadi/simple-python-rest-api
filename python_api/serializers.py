from rest_framework import serializers
from python_api import models

class HelloSerializers(serializers.Serializer):
  """serializers for name field for testing the api"""
  name = serializers.CharField(max_length=20)


class UserProfileSerializers(serializers.ModelSerializer):
  """Serializer a user profile object"""

  class Meta:
    model = models.UserProfile
    fields = ('id', 'email', 'name', 'password')
    extra_kwargs = {
      'password':{
        'write_only':True,
        'style': {'input_type': 'password'}
      }
    }

  def create(self,validated_data):
    """create and return a new user"""
    user = models.UserProfile.objects.create_user(
      email= validated_data['email'],
      name= validated_data['name'],
      password= validated_data['password']
      )
      
    return user