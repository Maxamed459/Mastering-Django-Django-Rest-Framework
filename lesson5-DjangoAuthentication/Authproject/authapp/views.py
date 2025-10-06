from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# For class based view[CBV]
from django.contrib.auth.mixins import LoginRequiredMixin
# For class based view[CBV]
from django.views import View
from django.contrib.auth.models import User
# import the RegisterForm from forms.py
from .forms import RegisterForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create(username=username, password=password)
            login(request, user)
            return redirect('home')
        form = RegisterForm()
        return render(request, 'auth/register.html', {
            'form': form
        })
    form = RegisterForm()
    return render(request, 'auth/register.html', {
        'form': form
    })

def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credintials"
    user = request.user

    return render(request, 'auth/login.html', {
        "error": error_message,
        'user': user
    })
        

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return redirect('home')


# home view 
# Using the decorator
@login_required
def home_view(request):
    return render(request, 'home/index.html')

