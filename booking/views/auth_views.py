from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        return render(request, 'registration/login.html', {'error': 'Invalid credentials'})

class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            return redirect('login')
        return render(request, 'registration/register.html', {'error': 'User already exists'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
