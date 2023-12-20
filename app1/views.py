# views.py
from django.shortcuts import render,redirect
from .forms import PersonForm,VehicleForm

def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'files/success_page.html', {'form': form})
    else:
        form = PersonForm()

    return render(request, 'files/Login.html', {'form': form})

def success_page(request):
    return render(request, 'files/success_page.html')


def create_vehicle(request):
    if request.method == 'POST':
        form1 = VehicleForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('create_person')
    else:
        form1 = VehicleForm()

    return render(request, 'files/Vehicle.html', {'form1': form1})



import logging

logger = logging.getLogger(__name__)

def your_function():
    # your code here
    logger.info('Your log message')    

