from django.shortcuts import (render, redirect)
from django.contrib import messages, auth
# importing default django user model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register(req):
        # Register User
    if req.method == 'POST':
        # Get form values
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():  # does it exist?
                messages.error(req, 'Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():  # does it exist?
                    messages.error(req, 'Email already registered')
                    return redirect('register')
                else:
                    # Passes validation
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Log in after register
                    # auth.login(req,user)
                    # messages.success(req, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        req, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(req, 'Passwords do not match')
        return redirect('register')
    else:
        return render(req, 'accounts/register.html')


def login(req):
    if req.method == 'POST':
        # log the user
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:  # if we find user
            auth.login(req, user)  # authenticate == log in
            messages.success(req, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(req, 'Invalid Credentials')
            return redirect('login')
    return render(req, 'accounts/login.html')


def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        messages.success(req, 'You are now logged out')
        return redirect('index')


@login_required(login_url='login')
def dashboard(req):
    return render(req, 'accounts/dashboard.html')
