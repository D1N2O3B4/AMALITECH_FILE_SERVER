from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View,TemplateView, DetailView
from .models import File
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.conf import settings
from django.core.mail import EmailMessage
from django.views.generic.edit import FormView


from django.shortcuts import redirect
import mimetypes

# Create your views here.

class HomeView(TemplateView):
    template_name = 'trip/index.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('file-list')
        return super().dispatch(request, *args, **kwargs)