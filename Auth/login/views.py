from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import signUpForm

# Create your views here.

def home(request):
    return render(request, "login/index.html")

def signup(request):
    
    form = signUpForm()
    
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, "login/signup.html", context)

def signin(request):
    return render(request, "login/signin.html")

def signout(request):
    pass

