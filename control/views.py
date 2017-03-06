from django.http import HttpResponse
from .models import alumno 

def index(request):
	all_alumno = alumno.object.all()
	html = ''
	for alumno in all_alumno:
		url = '/control/' + str(alumno.id) + '/'
		html += '<a href="' + url +'">' + alumno.nombre + '</a><br>'
	return HttpResponse(html)

def detail(request, alumno_id):
	return HttpResponse("<h2>Details for students: " + str(alumno_id) + "</h2>")
