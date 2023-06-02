from django.urls import path
from .import views

urlpatterns =[
    path('car_rentals/',views.car_rentals,name='car_rentals'),
    path('cars/',views.cars,name='cars'),
    path('car/<str:id>/',views.car,name='car'),
    path('rental_history/',views.rental_history,name='rental_history'),
    path('booking/',views.booking,name='booking'),
    path('delete_rental/<int:rental_id>/',views.delete_rental,name='delete_rental'),
    path('edit_rental/<int:rental_id>/',views.edit_rental,name='edit_rental'),

]