from django.shortcuts import render
from .models import Reservation

def home(request):
	all_reservations = Reservation.objects.all
	return render(request, 'home.html', {'all_reservations': all_reservations})


def add(request):
	return render(request, 'add.html', {})	
