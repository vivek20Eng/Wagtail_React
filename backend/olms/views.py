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

