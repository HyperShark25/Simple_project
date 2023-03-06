from django.shortcuts import render
from .serializers import DeviceSerializer
from .models import Device
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication, permissions
from rest_framework.authentication import authenticate


class DeviceView(APIView):
    # allowed_methods = 'list'
    # http_method_names = ['get']
    # queryset = Device.objects.all()
    # serializer_class = DeviceSerializer

    def get(self, request, *args, **kwargs):
        item = Device.objects.all()
        serializer = DeviceSerializer(item, many=True)
        return Response(serializer.data)
    #
    # def post(self, request, *args, **kwargs):
    #     serializer = DeviceSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
