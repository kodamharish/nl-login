from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from signin import settings
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
def login(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def home(request):
    return render(request, 'home.html')



