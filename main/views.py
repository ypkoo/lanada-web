from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def people(request):
	return render(request, 'people.html', {})

def awards(request):
	return render(request, 'awards.html', {})

def research(request):
	return render(request, 'research.html', {})

def about(request):
	return render(request, 'about.html', {})