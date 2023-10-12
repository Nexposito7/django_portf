from django.urls import path
from .views import render_posts, post_detail

#podemos identificar las urls con un nombre: 
app_name = 'blog'

# y lo definimos:
urlpatterns = [
    path('', render_posts, name='posts'),
    #todo lo que venga después de blog/ será considerado un id a buscar
    path('<int:post_id>', post_detail, name="post_detail") #y añadimos un nombre
    #buscará un entero, y después de la coma indicamos qué va ser renderizado
]
