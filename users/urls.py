from django.urls import path
from users import views

urlpatterns = [
    path('', views.home, name='users-home'),
]
