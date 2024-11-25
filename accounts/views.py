from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse

#create your views here
#Register
def register(request):
    """ Show the registion form """
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                user.save()
                
                # Display a message
                messages.success(request, "You have successfully created your account!")
                print(reverse('login'))
                return redirect('login')
            except:
                # Display a message if the above fails
                messages.error(request, "username already exist! use another username!")
        else:
                # Display a message saying password
                messages.error(request, "Your password do not match!")
    return render(request, 'accounts/register.html')

#login page
def login_view(request):
    """ show the login page """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        #check
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index_page')
        else:
            messages.error(request, "Invalid login credentials")
            
    return render(request, "accounts/login.html")
