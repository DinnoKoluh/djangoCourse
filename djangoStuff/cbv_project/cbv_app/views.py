from django.shortcuts import render
# for class base view
from django.views.generic import View

from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return render(request, 'index.html') # because no folder was created inside templates

class CBView(View):
    # has to be called get
    def get(self, request):
        return HttpResponse("ClASS BASE VIEWS")