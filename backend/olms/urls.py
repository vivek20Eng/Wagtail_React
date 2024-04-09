from django.urls import path
from . import views
# from auth import views

from authentication import views as auth_views

urlpatterns = [
    # path('hello-world/', views.hello_world, name='hello_world'),
    path('login/', auth_views.login_page, name='login_page'),
]