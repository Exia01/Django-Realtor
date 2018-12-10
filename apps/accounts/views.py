from django.shortcuts import (render, redirect)
from django.contrib import messages


def register(req):
    if req.method == 'POST':
        # Register User
        messages.error(req, 'Testing error message')
        return redirect('register')
    else:
        return render(req, 'accounts/register.html')


def login(req):
    if req.method == 'POST':
        # log the user
        print('SUBMITTED REG')
        return redirect('register')
    else:
        return render(req, 'accounts/register.html')
    return render(req, 'accounts/login.html')


def logout(req):
    return redirect('index')


def dashboard(req):
    return render(req, 'accounts/dashboard.html')
