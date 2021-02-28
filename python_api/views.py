from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
  """Test Api view"""

  def get(self, request, form=None):
    """Returns a list of APIView features"""
    an_apiview = [
      'Uses HTTP methods as function',
      'is similar to a traditional django view',
      'random test'
    ]
    return Response({'message': 'hello', 'an_apiview': an_apiview})