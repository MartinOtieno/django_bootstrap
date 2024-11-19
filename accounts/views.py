from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        else:
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            else:
                try:
                    # Create the user
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    
                    # Display success message and redirect
                    messages.success(request, "Account created successfully")
                    return redirect('myapp:home')
                except Exception as e:
                    # Log the error (optional)
                    print(e)
                    messages.error(request, "An error occurred during registration")
    
    # Render the registration form
    return render(request, 'accounts/register.html')

#login page
def login(request):
    """ Display the home page """
    return render(request, "accounts/login.html")
