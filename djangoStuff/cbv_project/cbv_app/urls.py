from django.urls import path

from cbv_app import views # instead . current folder name can be written  i.e. first_app

app_name = 'cbv_app' # to call it from .html files

urlpatterns = [
    path('', views.SchoolListView.as_view(), name = 'list'),
    #path(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail'),
    path('<int:pk>', views.SchoolDetailView.as_view(), name='detail'), # to link primary key to html
    path('create', views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.SchoolUpdateView.as_view(), name='update'), # to link primary key to html
    path('delete/<int:pk>', views.SchoolDeleteView.as_view(), name='delete'), # to link primary key to html



]