from django.urls import path

from . import views # instead . current folder name can be written  i.e. first_app

app_name = 'temp_app'

urlpatterns = [
    # path('', views.home, name = 'home'), # home page
    #path('', views.index, name='index'),
    path('temp_app/relative', views.relative, name = 'relative'),
    path('temp_app/other', views.other, name = 'other'),
    #path('user', views.user, name='user'),
    #path('user_input', views.user_input, name="user_input"),
    #path('new_user', views.new_user, name="new_user"),
]