from django.urls import path

from . import views # instead . current folder name can be written  i.e. first_app

urlpatterns = [
    path('', views.index, name='index'),
    path('formpage', views.form_name_view, name = 'form_name'),
]