from django.shortcuts import render
from django.http import HttpResponse
from ifsc.pages.competitions import Competitions
from ifsc.pages.athletes import Athletes

def index(request):
    print(request.path)
    path = request.path
    if path == '/scraper/':
        return render(request, 'index.html')

def competitions(request):
    competitions = Competitions()
    context = { 'competitions' : competitions.fetchCompetitions()}
    return render(request, 'competitions.html', context)

def athletes(request):
    athletes = Athletes()
    context = { 'athletes' : athletes.fetchAthletes()}
    return render(request, 'athletes.html', context)

