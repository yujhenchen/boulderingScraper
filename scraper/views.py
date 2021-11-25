from django.shortcuts import render
from django.http import HttpResponse
from ifsc.pages.competitions import Competitions

def index(request):

    competitions = Competitions()
    context = { 'competitions' : competitions.fetchCompetitions()}
    return render(request, 'index.html', context) 
