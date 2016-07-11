from django.shortcuts import render

# Create your views here.

def memory(request):
	from .models import Memory

	memory_list = Memory.objects.order_by('-date')

	context = {
		'memory_list': memory_list
	}

	return render(request, 'memory.html', context)

def memory_detail(request, title):
	from .models import Memory, Photo

	memory = Memory.objects.get(title=title)

	photo_list = Photo.objects.filter(memory=memory)

	context = {
		'memory': memory,
		'photo_list': photo_list,
	}

	return render(request, 'memory_detail.html', context)
