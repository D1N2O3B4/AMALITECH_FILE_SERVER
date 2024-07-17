from django.urls import path
from .views import HomeView, file_list, FileDetailView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('dashboard/',file_list,name = 'file-list'),
    path('dashboard/file/<int:pk>/',FileDetailView.as_view(),name='file-detail'),

]