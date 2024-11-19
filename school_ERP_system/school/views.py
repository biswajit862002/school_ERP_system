from django.shortcuts import render, HttpResponseRedirect
from .models import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

# this view function render the index page, where login and sign-up two links are there
def index(request):
    return render(request, 'school/index.html')

# this view function render the sign-up page, where user can create new account
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account Created successfully')
    else:
        fm = SignUpForm()
    
    return render(request, 'school/signup.html', {'form':fm})


# this view function render the login page, where after created successfully account he/she can login
def user_login(request):
    if not request.user.is_authenticated: # if any user can already logged in then login page is not showing for that user
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']

                user = authenticate(username=uname, password=upass)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!!')
                    return HttpResponseRedirect('/home/')
        else:
            fm = AuthenticationForm()
        return render(request, 'school/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/home/')

# This view function render the home page, only Authenticated user can access this page
def home(request):
    if request.user.is_authenticated: # is_authenticated is True when a user is Authenticate
        return render(request, 'school/home.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

# this view function is used for logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
