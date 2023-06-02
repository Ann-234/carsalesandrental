from django.shortcuts import  get_object_or_404, redirect, render
from django.core.mail import send_mail
import pandas as pd
import numpy as np
from django.contrib import messages
from rentals.forms import BookingForm

from .models import *


#create your views here
def car_rentals(request):
    cars=Car.objects.all().order_by('-created_at')[:3]

    context={
        'cars': cars
    }
    return render(request,'rentals/car_rentals.html',context)



def cars(request):
    cars=Car.objects.all()

    context={
        'cars':cars
    }
    return render(request,'rentals/cars.html',context)


def car(request,id):
    car=Car.objects.get(id=id)
    
    context={
        'car':car
    }
    return render(request,'rentals/car.html',context)



def rental_history(request):
    customer = Profile.objects.get(user=request.user)
    rentals = CarRental.objects.filter(customer=customer)


    context ={
        'rentals':rentals
    }
    return render(request, 'rentals/rental_history.html',context)


def booking(request):
    if request.method == 'POST':
        
        form = BookingForm(request.POST)
        if form.is_valid():
            rent = form.save(commit=False)
            rent.user = request.user
            rent.save()
            # Send an email notification to the user
            send_mail(
                 subject='Car Rental Confirmation',
                 message='Thank you for renting a car. We will attend to your request shortly.',
                 from_email= 'adeolahanna21@gmail.com',
                 recipient_list= ['hannajames630@gmail.com'],
                 fail_silently=False,
            )
            messages.success(request, 'Car rented successfully!')
            return redirect('rental_history')
    
    else:
        form = BookingForm()

    context ={
        'form':form
    }
          
    return render(request, 'rentals/car_booking.html', context)


def delete_rental(request, rental_id):
     rental = CarRental.objects.get(id=rental_id)
     rental.delete()
     return redirect('car_rentals')



def edit_rental(request, rental_id):
    rental = CarRental.objects.get(id=rental_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=rental)
        if form.is_valid():
            form.save()
            return redirect('car_rentals')
    else:
        form = BookingForm(instance=rental)
    return render(request, 'rentals/edit_rental.html', {'form': form})





    



     


      
      
   




   




