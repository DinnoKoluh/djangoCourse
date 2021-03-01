from django.shortcuts import render

from forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required # look up python decorators

# Create your views here.

def index(request):
    return render(request, 'user_app/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) # hashing the password
            user.save()

            # in case the data is not good we won't commit to the database immediatly, rather try to config the data
            profile = profile_form.save(commit=False) 
            # setting the one to one relationship
            profile.user = user

            # checking is the picture sent with request.FILES (because it is a file)
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'user_app/registration.html', {
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form,
    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)

        user = authenticate(username = username, password=password) # to authenticate a user

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index')) # redercting user after login, in this case they will be redirected to the homepage
            else:
                return HttpResponse("Account not active!") # in case the account is not active a blank page says it
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request, 'user_app/login.html', {})

# A decorator to have user to be logged in to do a view

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in!")