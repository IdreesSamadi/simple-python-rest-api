from django.urls import path
from python_api import views

urlpatterns = [
  path('hello-view/', views.HelloApiView.as_view())
]