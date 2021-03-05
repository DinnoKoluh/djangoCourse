from django.urls import path
from . import views #

app_name = 'groups' # to call it from .html files

urlpatterns = [
    path('', views.ListGroups.as_view(), name = 'all'),
    path('new', views.CreateGroup.as_view(), name='create'),
    path('postst/in/<slug:slug>', views.SingleGroup.as_view(), name='single'),
    
]