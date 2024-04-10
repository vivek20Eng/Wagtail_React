# views.py

from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def login_page(request):
    print(request,"reg==============")
    if request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=400)

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials.'}, status=401)

        login(request, user)
        return Response({'message': 'Login successful.'})
    else:
        return Response({'error': 'Method not allowed.'}, status=405)
