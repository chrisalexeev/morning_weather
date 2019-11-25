from django.urls import path
from users import views

urlpatterns = [
    path('', views.home, name='users-home'),
    path('profile/',views.update_profile, name='profile')
]
