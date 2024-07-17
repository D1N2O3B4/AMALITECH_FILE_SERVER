import django_filters
from .models import File
from django.db import models

class FileFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(method='filter_by_title')

    class Meta:
        model = File
        fields = ['title']

    def filter_by_title(self, queryset, name, value):
        words = value.split()
        query = models.Q()
        for word in words:
            query |= models.Q(title__istartswith=word)
        return queryset.filter(query)