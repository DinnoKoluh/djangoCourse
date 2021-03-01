from django.urls import path

from . import views # instead . current folder name can be written  i.e. first_app

urlpatterns = [
    path('', views.home, name = 'home'), # home page
    path('index', views.index, name='index'),
    path('user', views.user, name='user'),
    path('user_input', views.user_input, name="user_input"),
    path('new_user', views.new_user, name="new_user"),
]