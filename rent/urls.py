from django.urls import path
from . import views

urlpatterns = [
    # Other app-specific URL patterns go here
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('uav/', views.uav_list, name='uav_list'),
    path('uav/<int:pk>/', views.uav_detail, name='uav_detail'),
    path('uav/add/', views.uav_add, name='uav_add'),
    path('uav/update/<int:pk>/', views.uav_update, name='uav_update'),
    path('uav/delete/<int:pk>/', views.uav_delete, name='uav_delete'),
    path('rental-records/', views.rental_record_list, name='rental_record_list'),
    path('rental-records/<int:pk>/', views.rental_record_detail, name='rental_record_detail'),
    path('rental-records/<int:pk>/update/', views.rental_record_update, name='rental_record_update'),
    path('rental-records/<int:pk>/delete/', views.rental_record_delete, name='rental_record_delete'),
    path('uav/<int:uav_id>/rent/', views.rent_uav, name='rent_uav'),
    #path('rented-uavs/', views.rented_uavs, name='rented_uavs'),
]
