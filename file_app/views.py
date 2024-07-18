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
from .forms import EmailForm
import logging
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

#File Detail view
class FileDetailView(DetailView):
    model = File

#File Email view
class FileEmailView(FormView):
    template_name = 'file_app/file_email.html'
    form_class = EmailForm
    success_url = reverse_lazy('file-list')

    def form_valid(self, form):
        file_id = self.kwargs['pk']
        file = File.objects.get(pk=file_id)
        recipient = form.cleaned_data['recipient_email']
        message = form.cleaned_data['message']
        subject = file.title
        sender = settings.SERVER_EMAIL

        mime_type, _ = mimetypes.guess_type(file.file.path)

        email = EmailMessage(
            subject,
            message,
            sender,
            [recipient],
        )

        try:
            email.send()
            file.email_count += 1
            file.save()
        except Exception as e:
            logging.error('An error occured')

        return super().form_valid(form)

#File Download view
class FileDownloadView(View):
    def get(self, request, pk):
        file = get_object_or_404(File, pk=pk)
        file.download_count += 1
        file.save()

        response = FileResponse(file.file, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file.file.name}"'

        return response
