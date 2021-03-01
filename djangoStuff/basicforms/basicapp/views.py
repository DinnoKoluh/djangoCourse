from django.shortcuts import render
# importing forms.py file which contains the form class
from . import forms

# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html') # basicapp the name of the folder inside the templates folder which contains the html

def form_name_view(request):
    form = forms.FormName

    # to check if someone is posint/sending/hit submit something
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            # Do something here 
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
        else:
            print("FORM NOT OK!")

    return render(request, 'basicapp/form_page.html', {
        'form': form
    })
 