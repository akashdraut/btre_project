from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    ''' To take info and register user '''
    if request.method == 'POST':
        # Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password matches
        if password == password2:
            # Check if username is exists
            if User.objects.filter(username=name).exists():
                messages.error(request, "Username is already taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is already registered")
                    return redirect('register')
                else:
                    return
        else:
            messages.error(request, "Password do not matched")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    ''' Login user by email and password '''
    if request.method == 'POST':
        # login Logic
        return
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    ''' Logout user '''
    return redirect('index')

def dashboard(request):
    ''' Redirect to dashboard '''
    return render(request, 'accounts/dashboard.html')
