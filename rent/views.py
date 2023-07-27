from django.shortcuts import render, redirect, get_object_or_404
from .models import UAV, RentalRecord
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from .models import RentalRecord
from .forms import RentalRecordForm
from django.http import Http404
from .forms import UAVForm
from .models import RentalRecord
from .filters import RentalRecordFilter
from .models import UAV
from .filters import UAVFilter


login_required
def uav_list(request):
    uav_filter = UAVFilter(request.GET, queryset=UAV.objects.all())
    return render(request, 'uav_list.html', {'uav_filter': uav_filter})

@login_required
def uav_detail(request, pk):
    uav = get_object_or_404(UAV, pk=pk)
    return render(request, 'uav_detail.html', {'uav': uav})

def uav_add(request):
    if not request.user.is_superuser:  # Changed to check for superuser
        return redirect('uav_list')

    if request.method == 'POST':
        form = UAVForm(request.POST, request.FILES)  # Pass request.FILES for image upload
        if form.is_valid():
            form.save()
            return redirect('uav_list')
    else:
        form = UAVForm()

    return render(request, 'uav_add.html', {'form': form})

@login_required
def uav_update(request, pk):
    uav = get_object_or_404(UAV, pk=pk)
    
    # Check if the user is an admin or the owner of the UAV
    if not request.user.is_admin and uav.created_by != request.user:
        return redirect('uav_list')
    
    if request.method == 'POST':
        uav.brand = request.POST.get('brand')
        uav.model = request.POST.get('model')
        uav.weight = float(request.POST.get('weight'))
        uav.category = request.POST.get('category')
        uav.save()
        return redirect('uav_list')
    return render(request, 'uav_update.html', {'uav': uav})

@login_required
def uav_delete(request, pk):
    uav = get_object_or_404(UAV, pk=pk)

    # Check if the user is an admin or the owner of the UAV
    if not request.user.is_admin and uav.created_by != request.user:
        return redirect('uav_list')

    if request.method == 'POST':
        uav.delete()
        return redirect('uav_list')
    return render(request, 'uav_delete.html', {'uav': uav})



def rental_record_list(request):
    rental_records = RentalRecord.objects.all()
    rental_record_filter = RentalRecordFilter(request.GET, queryset=rental_records)
    context = {
        'rental_records': rental_record_filter.qs,
        'rental_record_filter': rental_record_filter,
    }
    return render(request, 'rental_record_list.html', context)

def rental_record_detail(request, pk):
    rental_record = get_object_or_404(RentalRecord, pk=pk)
    return render(request, 'rental_record_detail.html', {'rental_record': rental_record})

@login_required
def rental_record_update(request, pk):
    rental_record = get_object_or_404(RentalRecord, pk=pk)

    # Check if the requesting user is the owner of the rental record
    if rental_record.renting_member != request.user:
        raise Http404("You are not allowed to update this rental record.")

    if request.method == 'POST':
        form = RentalRecordForm(request.POST, instance=rental_record)
        if form.is_valid():
            form.save()
            return redirect('rental_record_list')
    else:
        form = RentalRecordForm(instance=rental_record)

    return render(request, 'rental_record_update.html', {'form': form, 'rental_record': rental_record})


@login_required
def rental_record_delete(request, pk):
    rental_record = get_object_or_404(RentalRecord, pk=pk)
    
    # Check if the requesting user is the owner of the rental record
    if rental_record.renting_member != request.user:
        raise Http404("You are not allowed to delete this rental record.")
    
    if request.method == 'POST':
        rental_record.delete()
        return redirect('rental_record_list')
    return render(request, 'rental_record_delete.html', {'rental_record': rental_record})


@login_required
def rent_uav(request, uav_id):
    uav = get_object_or_404(UAV, pk=uav_id)
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        renting_member = request.user
        RentalRecord.objects.create(uav=uav, start_date=start_date, end_date=end_date, renting_member=renting_member)
        return redirect('rental_record_list')
    return render(request, 'rent_uav.html', {'uav': uav})

@login_required
def rented_uavs(request):
    rented_uavs = RentalRecord.objects.filter(renting_member=request.user)
    return render(request, 'rented_uavs.html', {'rented_uavs': rented_uavs})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('uav_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
