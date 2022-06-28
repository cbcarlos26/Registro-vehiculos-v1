from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('inicio')
        else:
            messages.success(request, 'Compruebe usuario o contrasena')
            return redirect('login')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')