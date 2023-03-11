from django.shortcuts import render, redirect
from .serializers import DeviceSerializer
from .models import Device, New, LOD
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import authenticate
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import DeviceForm


class DeviceView(APIView):

    def get(self, request, *args, **kwargs):
        item = Device.objects.all()
        serializer = DeviceSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


def second(request, pk):
    a = Device.objects.get(id=pk)
    return render(request, 'second.html', {'a': a})


def dragon(request):
    a = Device.objects.all()
    return render(request, 'dragon.html', {'a': a})


def like(request):
    item = LOD.objects.all()
    return render(request, 'lod.html', {'item': item})


def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        email = request.POST['Email']
        password = request.POST['Password']
        password2 = request.POST['Password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Used')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords don't match")
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dragon')

        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('dragon')


# class MainViewClass(ListView):
#     template_name = 'hello.html'
#     model = New
#     context_object_name = 'item'


# def deviceform(request):
#     context = {}
#     context['form'] = DeviceForm()
#     return render(request, 'hello.html', context)


def myform(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('hello')
    else:
        form = DeviceForm()
    return render(request, 'hello.html', {'form': form})
