from django.urls import path

from user_app import views # instead . current folder name can be written  i.e. first_app

app_name = 'user_app'

urlpatterns = [
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    
]