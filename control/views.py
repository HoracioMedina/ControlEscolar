from django.http import Http404
from django.shortcuts import render
from .models import alumno 

def index(request):
	all_alumno = alumno.objects.all()
	return render(request, 'control/index.html', {'all_alumno': all_alumno})

def detail(request, numControl):
	try:
		alumnos = alumno.objects.get(pk=numControl)
	except alumno.DoesNotExist:
		raise Http404("Alumno no existe")
	return render(request, 'control/detail.html',{'alumno': alumnos})
