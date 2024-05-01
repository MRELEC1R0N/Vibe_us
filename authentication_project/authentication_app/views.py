from django.shortcuts import render, redirect
from .models import User

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username, password=password).exists():
            request.session['username'] = username
            return redirect('home')
        else:
            error = "Invalid username or password."
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        new_username = request.POST.get('new-username')
        new_password = request.POST.get('new-password')
        if not User.objects.filter(username=new_username).exists():
            User.objects.create(username=new_username, password=new_password)
            return redirect('login')
        else:
            error = "Username already exists."
            return render(request, 'signup.html', {'error': error})
    return render(request, 'signup.html')

def home(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    return render(request, 'home.html', {'username': username})

def logout(request):
    request.session.pop('username', None)
    return redirect('login')
