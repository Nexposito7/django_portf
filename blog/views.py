from django.shortcuts import render, get_object_or_404
from .models import Post

#vista que reneriza todas las publicaciones:
def render_posts(request): #esta func retorna el post.html
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

#vista para renderizar un detalle de publicación:
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    #le pasam el modelo q queremos buscar yqué querem buscar(conun primarykey)
    return render(request, 'post_detail.html', {"post": post})




