from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from python_api import serializers


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