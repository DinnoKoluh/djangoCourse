from django.shortcuts import render

from django.http import HttpResponse

from first_app.models import Topic, AccessRecord, Webpage, User

from first_app import forms

from first_app.model_forms import NewUserForm
# Create your views here.

# a view called index (a function), each view takes in one argument
# each view must return a HttpResponse object
def index(request):
    webpages_list = AccessRecord.objects.order_by('date') # order_by and sql command
    date_dict = {
        'access_records': webpages_list
    }
    #return HttpResponse("<em> Hello World Bitches </em>")
    # insert_me is the name of the variable inside the index.html file from the templates folder
    my_dict = {
        'insert_me': "hello I am from views.py motherfucker"
        }
    #return render(request, 'first_app/index.html', context=my_dict) # first_app from the templates folder
    return render(request, 'first_app1/index.html', context=date_dict) #'first_app1' takes the name of the folder from the templates folder

def user(request):

    user_info = User.objects.order_by('f_name')
    for i in range(len(user_info)):
        user_info[i].email = "{x}.{y}@{z}".format(x = user_info[i].f_name.lower(), y = user_info[i].l_name.lower(), z = user_info[i].email.split("@")[1])
        #user_info[i].save() # when you save it once it's done
    # print(user_info[1].f_name)
    #user_info[:].save()
    user_dict = {
        'user_info_key': user_info
    }
    return render(request, 'first_app1/user_info.html', context=user_dict)

def home(request):
    return HttpResponse("<h1> <em> Welcome to the home page </em> </h1>")

def user_input(request):
    form = forms.UserInput

    # to check if someone is posint/sending/hit submit something
    if request.method == 'POST':
        form = forms.UserInput(request.POST)
        if form.is_valid():
            # Do something here 
            full_name = form.cleaned_data['name'].split(" ")
            f_name = full_name[0]
            l_name = full_name[1]
            email = form.cleaned_data['email']
            # save user info
            User.objects.create(f_name = f_name, l_name = l_name, email = email)
            return index(request)
        else:
            print("FORM NOT OK!")

    return render(request, 'first_app1/user_input.html', {
        'form': form
    })


def new_user(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save(commit = True) # to commit data to database
            return index(request)
        else:
            print("Form is invalid")
    
    return render(request, 'first_app1/new_user.html', {
        'form': form
    })