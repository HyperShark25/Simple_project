from django.urls import path
from .views import DeviceView, MainViewClass
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', DeviceView.as_view()),     # path('api/', views.DeviceView.as_view(), name='api_view')
    # path('api/token/', obtain_auth_token, name='obtain'),
    path('dragon', views.dragon, name='dragon'),
    path('dragon/<int:pk>', views.second, name='second'),
    path('hello', MainViewClass.as_view()),
    path('dragon/register', views.register, name='register'),
    path('dragon/login', views.login, name='login'),
    path('dragon/logout', views.logout, name='logout')
]
