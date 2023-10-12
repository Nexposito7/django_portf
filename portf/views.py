from django.shortcuts import render #render es básicamente para decirle qué pag va a ser mostrada
from .models import Project

# Create your views here.
def home(request): 
    projects = Project.objects.all() #trae todos los proy guardados en ese momento
    return render(request, 'home.html', {'dicprojects': projects}) # render ya conoce la carpeta templates
    # y le pasamos un dic con una propied llamada projects 
