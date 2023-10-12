from django.db import models
from django.db.models.fields import CharField, URLField #import campos 
from django.db.models.fields.files import ImageField #para las imág

# Create your models here.
class Project(models.Model): #a través de models hereda una clase llamada Model 
    #empezamos a definir qué queremos guardar dentro del proj 
    #para cada proj va a tener unas propiedades
    title = CharField(max_length=100) #de tipo CharField 
    description = CharField(max_length=250)
    image = ImageField(upload_to='portf/images/')
    url = URLField(blank=True) #*min18



