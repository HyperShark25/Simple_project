from django.urls import path
from .views import DeviceView
from . import views


urlpatterns = [
    path('', DeviceView.as_view()),     # path('api/', views.DeviceView.as_view(), name='api_view')
]
