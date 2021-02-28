from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
  """serializers for name field for testing the api"""
  name = serializers.CharField(max_length=20)

  