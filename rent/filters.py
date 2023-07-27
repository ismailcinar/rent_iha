# filters.py
import django_filters
from .models import UAV
from .models import RentalRecord
from django.db.models import Q

class UAVFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(lookup_expr='icontains')  # Filter by brand (case-insensitive contains)
    model = django_filters.CharFilter(lookup_expr='icontains')  # Filter by model (case-insensitive contains)
    weight = django_filters.NumberFilter(lookup_expr='exact')  # Filter by weight (exact match)
    category = django_filters.CharFilter(lookup_expr='icontains')  # Filter by category (case-insensitive contains)
    search = django_filters.CharFilter(method='filter_search')  # Custom search filter for brand, model, and category

    class Meta:
        model = UAV
        fields = ['brand', 'model', 'weight', 'category']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(brand__icontains=value) |
            Q(model__icontains=value) |
            Q(category__icontains=value)
        )
    
    

class RentalRecordFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='start_date', lookup_expr='gte', label='Start Date (Min)')  # Filter by start date (greater than or equal to)
    end_date = django_filters.DateFilter(field_name='end_date', lookup_expr='lte', label='End Date (Max)')  # Filter by end date (less than or equal to)
    q = django_filters.CharFilter(method='search_filter', label='Search')  # Custom search filter for UAV brand and Renting Member username
    uav__brand = django_filters.CharFilter(field_name='uav__brand', lookup_expr='icontains', label='UAV Brand')  # Filter by UAV brand (case-insensitive contains)
    renting_member__username = django_filters.CharFilter(field_name='renting_member__username', lookup_expr='icontains', label='Renting Member Username')  # Filter by Renting Member username (case-insensitive contains)
    
    class Meta:
        model = RentalRecord
        fields = []

    def search_filter(self, queryset, name, value):
        # Custom search filter that performs OR operation on UAV brand and Renting Member username
        return queryset.filter(uav__brand__icontains=value) | queryset.filter(renting_member__username__icontains=value)
    