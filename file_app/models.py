from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
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



    def __str__(self):
        return f"Filename: {self.title}| FileType:{self.file_format} | Download_count{self.download_count}| Email_count: {self.email_count}"