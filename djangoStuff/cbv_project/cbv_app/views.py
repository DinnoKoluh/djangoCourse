from django.shortcuts import render
# for class base view
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.http import HttpResponse

from cbv_app import models
# for deleting
from django.urls import reverse_lazy
# Create your views here.

# def index(request):
#     return render(request, 'index.html') # because no folder was created inside templates

# using class view
# class CBView(View):
#     # has to be called get
#     def get(self, request):
#         #return HttpResponse("ClASS BASE VIEWS")
#         return render(request, 'index.html')
 
#using templates view
class IndexView(TemplateView):
    template_name = 'index.html'

    # kvargs --> key word arguments, *args (for only arugments)
    # *args is similar to matlabs narg, the functions arguments are sent in as a tuple
    # **kvargs gives us a dictionary of arguments
    def get_context_data(self, **kvargs):
        context = super().get_context_data(**kvargs)
        context['injectme'] = 'Basic injection'
        return context


class SchoolListView(ListView):
    model = models.School
    # this return a context dictionary with name school_list (what we called in the schol_list.html file)
    # if we want to return a custom name of the dictionary
    context_object_name = 'schools'

class SchoolDetailView(DetailView):
    # this would return a context dictionary with the lowercase name of the model which is school
    model = models.School
    template_name = 'cbv_app/school_detail.html'

    context_object_name = 'school_detail'

# a class to create a view/to add new users/info to database
class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School
    template_name = 'cbv_app/create_school.html'

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School
    template_name = 'cbv_app/create_school.html'

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('cbv_app:list')
    template_name = 'cbv_app/school_delete.html'