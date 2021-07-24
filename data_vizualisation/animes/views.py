
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


def vf_animes(request):
	animes = Anime.objects.all()
	episodes = Episode.objects.all()
	data = {'animes': animes, 'episodes': episodes}
	return render(request, "show_vf_animes.html", data)


def vostfr_animes(request):
	animes = Anime.objects.all()
	episodes = Episode.objects.all()
	data = {'animes': animes, 'episodes': episodes}
	return render(request, "show_vostfr_animes.html", data)

def status_in_progress(request):
	animes = Anime.objects.all()
	episodes = Episode.objects.all()
	data = {'animes': animes, 'episodes': episodes}
	return render(request, "show_animes_in_progress.html", data)

def status_finished(request):
	animes = Anime.objects.all()
	episodes = Episode.objects.all()
	data = {'animes': animes, 'episodes': episodes}
	return render(request, "show_animes_finished.html", data)


def search_animes(request):
	if request.method == "POST":
		searched = request.POST['searched']
		animes = Anime.objects.filter(anime_name__contains=searched)

		return render(request,
		'search_animes.html',
		{'searched':searched,
		'animes':animes})
	else:
		return render(request, 
		'search_animes.html',
		{})


def show_anime(request,anime_id):
	anime = Anime.objects.get(id=anime_id)
	episodes = Episode.objects.all()
	t = loader.get_template('show_anime.html')
	if anime.id == anime_id:
		data = {'anime': anime, 'episodes': episodes}
		return HttpResponse(t.render(data, request))



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


