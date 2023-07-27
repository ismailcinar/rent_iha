from django.contrib import admin

from .models import UAV,RentalRecord
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_admin']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(RentalRecord)
admin.site.register(UAV)