from .forms import UserRegisterForm
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login.')
            return redirect('users-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})