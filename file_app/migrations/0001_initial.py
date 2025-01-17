# Generated by Django 5.0.6 on 2024-07-17 09:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('file_format', models.CharField(choices=[('image', 'Image'), ('txt', 'Text File'), ('pdf', 'PDF'), ('doc', 'Word Document'), ('audio', 'Audio'), ('video', 'Video')], default='image', max_length=10)),
                ('file', models.FileField(upload_to='files')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('download_count', models.PositiveIntegerField(default=0)),
                ('email_count', models.PositiveIntegerField(default=0)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
