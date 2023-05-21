from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email taken')
                return redirect('index')
            else:
    # Create a new user
                 user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,email=email,password=password)
                 user.save();
                 print("user created")
                 messages.success(request, 'Registration successful. Please log in.')
                 return redirect('login')  # Redirect to the login page
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Invalid credentials')
                return redirect('login')
        else:
            messages.info(request, 'Please provide username and password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


