from django.urls import path
from .views import DeviceView
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', DeviceView.as_view()),     # path('api/', views.DeviceView.as_view(), name='api_view')
    path('api/token/', obtain_auth_token, name='obtain'),
    path('dragon', views.dragon, name='dragon'),
    path('dragon/<int:pk>', views.second, name='second')
]
