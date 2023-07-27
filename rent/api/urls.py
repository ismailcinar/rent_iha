# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Your existing URL patterns
    # ...
    # Add the API endpoints for UAV model
    path('uav/', views.UAVListView.as_view(), name='uav-list'),
    path('uav/<int:pk>/', views.UAVDetailView.as_view(), name='uav-detail'),
    # Add the API endpoints for RentalRecord model
    path('rental-records/', views.RentalRecordListView.as_view(), name='rental-record-list'),
    path('rental-records/<int:pk>/', views.RentalRecordDetailView.as_view(), name='rental-record-detail'),
]
