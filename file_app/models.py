from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

# Create your models here.

def check_file_format(value, file_format):
    extension = value.name.split('.')[-1].lower()
    valid_extensions = {
        'image': ['jpg', 'jpeg', 'png', 'gif'],
        'txt': ['txt'],
        'pdf': ['pdf'],
        'doc': ['doc', 'docx'],
        'audio': ['mp3', 'wav'],
        'video': ['mp4', 'avi', 'mov']
    }
    if extension not in valid_extensions.get(file_format, []):
        raise ValidationError(f'Invalid file format for {file_format}.')

class File(models.Model):
    FILE_FORMAT = (
        ('image', 'Image'),
        ('txt', 'Text File'),
        ('pdf', 'PDF'),
        ('doc', 'Word Document'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    file_format = models.CharField(max_length=10, choices=FILE_FORMAT, default='image')
    file = models.FileField(upload_to='files')
    upload_date = models.DateTimeField(auto_now_add=True)
    download_count = models.PositiveIntegerField(default=0)
    email_count = models.PositiveIntegerField(default=0)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='file')

    def clean(self):
        check_file_format(self.file, self.file_format)
        super().clean()

    def __str__(self):
        return f"Filename: {self.title}| FileType:{self.file_format} | Download_count{self.download_count}| Email_count: {self.email_count}"