
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile, Follow
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import never_cache

@never_cache
def home_view(request):
    return render(request, 'home.html')

@never_cache
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')

        # Check if the user already exists
        if User.objects.filter(username=name).exists():
            messages.error(request, "Username already exists!")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
        else:
            # Create new user
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('signIn')  # Redirect to sign-in page after registration

    return render(request, 'registration.html')


@never_cache
def signIn_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)  # Fetch user by email
            username = user.username  # Extract the username
            user = authenticate(request, username=username, password=password)
        except User.DoesNotExist:
            user = None  # User does not exist

        if user is not None:
            login(request, user)
            return redirect('header')  # Redirect to header after successful login
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'signIn.html')


@never_cache
def header_view(request):
    return render(request, 'header.html')





