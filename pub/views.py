from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def pub(request):
	return redirect('book/')

def book(request):
	return render(request, 'book.html', {})

def journal(request):
	from .models import JournalPaper

	paper_list = JournalPaper.objects.order_by('-date')

	context = {
		'paper_list': paper_list
	}

	return render(request, 'journal.html', context)

## merge this with conference_pdf
def journal_pdf(request, title):

	with open('media/paper/journal/%s' % title, 'rb') as pdf:
		response = HttpResponse(pdf.read(),content_type='application/pdf')
		response['Content-Disposition'] = 'filename=%s' % title
		return response
	pdf.closed

def conference(request):
	from .models import ConferencePaper

	paper_list = ConferencePaper.objects.order_by('-date')

	context = {
		'paper_list': paper_list
	}

	return render(request, 'conference.html', context)

def conference_pdf(request, title):

	with open('media/paper/conference/%s' % title, 'rb') as pdf:
		response = HttpResponse(pdf.read(),content_type='application/pdf')
		response['Content-Disposition'] = 'filename=%s' % title
		return response
	pdf.closed


def upload(request):
	return render(request, 'upload.html')