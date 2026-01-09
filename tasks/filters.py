import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    created_from = django_filters.DateFilter(
        field_name='created_at', lookup_expr='gte'
    )
    created_to = django_filters.DateFilter(
        field_name='created_at', lookup_expr='lte'
    )

    class Meta:
        model = Task
        fields = ['title']
