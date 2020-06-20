from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Q
from datetime import date
from django.views.generic import TemplateView, ListView

'''
def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    qs = Reservation.objects.all()    
    date = request.GET.get('date')
        
    if is_valid_queryparam(date):
        qs = qs.filter(date=date)

    return qs
'''

def home(request):
	today = date.today()
	all_reservations = Reservation.objects.filter(date=today).order_by('time')
	return render(request, 'home.html', {'all_reservations': all_reservations})

def add(request):
	if request.method == "POST":
		form = ReservationForm(request.POST or None)
		res_name = request.POST.get('name')		
		if form.is_valid():			
			form.save()
			messages.success(request, (res_name + ' Reservation has been added!'))			
			return redirect('home')			
		else:		
			today = date.today()
			for_date = today.strftime("%Y-%m-%d")
			maxdate = '2020-10-31'	
			messages.error(request, ('Date and time already reserved.  Please try again.'))	
			return render(request, 'add.html', {'for_date': for_date, 'maxdate': maxdate})		
	else:
		today = date.today()
		for_date = today.strftime("%Y-%m-%d")
		maxdate = '2020-10-31'
		return render(request, 'add.html', {'for_date': for_date, 'maxdate': maxdate})	

def edit(request, list_id):
	if request.method == "POST":
		current_reservation = Reservation.objects.get(pk=list_id)		
		form = ReservationForm(request.POST or None, instance=current_reservation)
		res_name = request.POST.get('name')	
		if form.is_valid():
			form.save()
			messages.success(request, (res_name + ' Reservation has been edited!'))
			return redirect('home')			
		else:				
			messages.error(request, ('Date and time already reserved.  Please try again.'))	
			return render(request, 'home.html', {})
			
	else:
		get_reservation = Reservation.objects.get(pk=list_id)
		return render(request, 'edit.html', {'get_reservation': get_reservation})

def delete(request, list_id):
	if request.method == "POST":
		current_reservation = Reservation.objects.get(pk=list_id)		
		current_reservation.delete()
		messages.success(request, ('Reservation has been deleted!')) 
		return redirect('home')		
	else:
		messages.error(request, ('Nothing to see here...'))			
		return render(request, 'home.html', {})	

def by_date(request):
	today = date.today()
	for_date = today.strftime("%Y-%m-%d")
	maxdate = '2020-10-31'		
	return render(request, "by_date.html", {'for_date': for_date, 'maxdate': maxdate})	

def list_all(request):	
	today = date.today()
	for_date = today.strftime("%Y-%m-%d")
	all_reservations = Reservation.objects.filter(date__gte=for_date).order_by('date','time')
	return render(request, 'list_all.html', {'all_reservations': all_reservations})

'''
class ByDateView(TemplateView):
    template_name = 'by_date.html'
'''

class SearchResultsView(ListView):
	model = Reservation
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		object_list = Reservation.objects.filter(
			Q(date__icontains=query)
		)
		return object_list