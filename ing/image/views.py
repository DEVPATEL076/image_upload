from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *

def Image(request):
	if request.method=='POST':
		form=img_stor(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('view')
	else:
		form=img_stor()

	return render(request, "home.html", {'form' : form})

def MyView(request):
    query_results = demo.objects.all()
    context= {'results': query_results}

    return render(request, 'view.html', context)