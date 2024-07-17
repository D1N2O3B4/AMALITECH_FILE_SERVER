from django.urls import path
from .views import HomeView, file_list

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('dashboard/',file_list,name = 'file-list'),

]