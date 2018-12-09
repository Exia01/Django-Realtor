from django.shortcuts import (render, redirect)


def register(req):
    if req.method == 'POST':
        # Register User
        print('SUBMITTED REG')
        return redirect('register')
    else:
        return render(req, 'accounts/register.html')


def login(req):
    if req.method == 'POST':
        # Register User
        print('SUBMITTED REG')
        return redirect('register')
    else:
        return render(req, 'accounts/register.html')
    return render(req, 'accounts/login.html')


def logout(req):
    return redirect('index')


def dashboard(req):
    return render(req, 'accounts/dashboard.html')
