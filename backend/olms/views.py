from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'message': 'Hello, world!'})

@api_view(['GET'])
# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "GET":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return Response({'message': username})
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return Response({'message': 'Hello, world!'})
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return Response({'message': 'Hello, world!'})
     
    # Render the login page template (GET request)
    return render(request, 'login.html')