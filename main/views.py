from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'main/index.html', {})

def people(request):
	return render(request, 'main/people.html', {})

def awards(request):
	return render(request, 'main/awards.html', {})

def research(request):
	return render(request, 'main/research.html', {})