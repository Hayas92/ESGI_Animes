
import calendar

from django.shortcuts import render, redirect
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Anime,Episode
from django.http import HttpResponse, HttpRequest
from django.template import loader
# Import Pagination Stuff
from django.core.paginator import Paginator

# Generate a PDF File Anime List

def animes(request):
	animes = Anime.objects.all()
	episodes = Episode.objects.all()
	data = {'animes': animes, 'episodes': episodes}
	return render(request,"anime_list.html",data)


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	month = month.capitalize()

	# Get current year
	current_year = datetime.now().year

	# Get current time
	time = datetime.now().strftime('%H:%M')
	return render(request, 
		'home.html', {
		"year": year,
		"month": month,
		"current_year": current_year,
		"time":time,
		})


