from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages

def home(request):
	all_reservations = Reservation.objects.all
	return render(request, 'home.html', {'all_reservations': all_reservations})


def add(request):
	if request.method == "POST":
		form = ReservationForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Reservation Has Been Added!'))
			return redirect('home')
		else:
			messages.success(request, ('Seems Like There Was An Error...'))	
			return render(request, 'add.html', {})	
	else:
		return render(request, 'add.html', {})	

def edit(request, list_id):
	if request.method == "POST":
		current_reservation = Reservation.objects.get(pk=list_id)
		form = ReservationForm(request.POST or None, instance=current_reservation)
		if form.is_valid():
			form.save()
			messages.success(request, ('Reservation Has Been Edited!'))
			return redirect('home')
		else:
			messages.success(request, ('Seems Like There Was An Error...'))	
			return render(request, 'edit.html', {})	
	else:
		get_reservation = Reservation.objects.get(pk=list_id)
		return render(request, 'edit.html', {'get_reservation': get_reservation})

def delete(request, list_id):
	if request.method == "POST":
		current_reservation = Reservation.objects.get(pk=list_id)
		current_reservation.delete()
		messages.success(request, ('Reservation Has Been Deleted!'))
		return redirect('home')
	else:
		messages.success(request, ('Nothing To See Here...'))	
		return redirect('home')			

