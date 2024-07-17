from django.urls import path
from .views import HomeView, file_list, FileDetailView, FileEmailView, FileDownloadView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('dashboard/',file_list,name = 'file-list'),
    path('dashboard/file/<int:pk>/',FileDetailView.as_view(),name='file-detail'),
    path('dashboard/file/<int:pk>/email/', FileEmailView.as_view(), name='file-email'),
    path('dashboard/file/<int:pk>/download/', FileDownloadView.as_view(), name='file-download'),
]