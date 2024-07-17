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
from .filters import FileFilter
from django.shortcuts import redirect
import mimetypes

# Create your views here.

#Homeview for index.html
class HomeView(TemplateView):
    template_name = 'file_app/index.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('file-list')
        return super().dispatch(request, *args, **kwargs)

#File list view for dashboard
def file_list(request):
    files = File.objects.all()
    myFilter = FileFilter(request.GET, queryset=File.objects.all())
    context = {
        'files':files,
        'myFilter':myFilter,
    }
    return render(request,'file_app/file_list.html',context)

