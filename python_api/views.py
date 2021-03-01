from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from python_api import serializers
from python_api import models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from python_api import permissions
from rest_framework import filters


class HelloApiView(APIView):
  """Test Api view"""
  serializer_class = serializers.HelloSerializers

  def get(self, request, form=None):
    """Returns a list of APIView features"""
    an_apiview = [
      'Uses HTTP methods as function',
      'is similar to a traditional django view',
      'random test'
    ]
    return Response({'message': 'hello', 'an_apiview': an_apiview})

  def post(self, request):
    """create a hello message with user name"""
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'
      return Response({message: message})

    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk=None):
    """Handle updating an object"""
    return Response({'method': 'PUT'})

  def patch(self, request, pk=None):
    """Handle partial updating an object"""
    return Response({'method': 'Patch'})

  def delete(self, request, pk=None):
    """delete an object"""
    return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
  """Test API view set"""
  serializer_class = serializers.HelloSerializers

  def list(self, request):
    """return a hello message"""
    an_apiview = [
      'Uses HTTP methods as function',
      'is similar to a traditional django view',
      'random test'
    ]
    return Response({'message': 'hello', 'an_apiview': an_apiview})

  def create(self, request):
    """create a new hello message"""
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'
      return Response({message: message})

    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def retrieve(self, request, pk=None):
    """Handle getting an object by its id"""
    return Response({'http_method': 'get'})

  def update(self, request, pk=None):
    """Handle updating an object"""
    return Response({'http_method': 'Put'})

  def destroy(self, request, pk=None):
    """delete an object"""
    return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
  """Handle create and update profile"""
  serializer_class = serializers.UserProfileSerializers
  queryset = models.UserProfile.objects.all()
  authentication_classes = (TokenAuthentication,) 
  permission_classes = (permissions.UpdateOwnProfile,)
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name','email')