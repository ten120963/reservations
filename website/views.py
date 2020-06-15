from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Q
from datetime import date

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    qs = Reservation.objects.all()    
    date = request.GET.get('date')
        
    if is_valid_queryparam(date):
        qs = qs.filter(date=date)

    return qs

def home(request):
	today = date.today()
	all_reservations = Reservation.objects.filter(date=today).order_by('time')
	return render(request, 'home.html', {'all_reservations': all_reservations})

def add(request):
	if request.method == "POST":
		form = ReservationForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Reservation has been added!'))
			#color = "success"
			return redirect('home')
			#return render(request, 'home.html', {'color': color})			
		else:
			#color = "danger"
			messages.success(request, ('Date and time already reserved.  Please try again.'))	
			#return render(request, 'add.html', {'color': color})	
			return render(request, 'add.html', {})
	else:
		return render(request, 'add.html', {})	

def edit(request, list_id):
	if request.method == "POST":
		current_reservation = Reservation.objects.get(pk=list_id)
		form = ReservationForm(request.POST or None, instance=current_reservation)
		if form.is_valid():
			form.save()
			messages.success(request, ('Reservation has been edited!'))
			#color = "success"
			return redirect('home')
			#return render(request, 'home.html', {'color': color})
		else:
			#color = "danger"
			messages.success(request, ('Seems like there was an error...'))	
			#return render(request, 'edit.html', {'color': color})
			return render(request, 'edit.html', {'color': color})	
	else:
		get_reservation = Reservation.objects.get(pk=list_id)
		return render(request, 'edit.html', {'get_reservation': get_reservation})

def delete(request, list_id):
	if request.method == "POST":
		current_reservation = Reservation.objects.get(pk=list_id)
		current_reservation.delete()
		messages.success(request, ('Reservation has been deleted!')) 
		#color = "success"
		return redirect('home')
		#return render(request, 'home.html', {'color': color})
	else:
		#color = "danger"
		messages.success(request, ('Nothing to see here...'))	
		return redirect('home')	
		#return render(request, 'home.html', {'color': color})	

def by_date(request):
	
	qs = filter(request)
	context = {
		'queryset': qs,		
	}
	return render(request, "by_date.html", context)

def list_all(request):	
	all_reservations = Reservation.objects.order_by('date','time')
	return render(request, 'list_all.html', {'all_reservations': all_reservations})
