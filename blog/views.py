# blog/views.py
from django.shortcuts import render
from .models import Post  # Si estás usando el modelo 'Post'

def post_list(request):
    posts = Post.objects.all()  # Obtiene todos los posts de la base de datos
    return render(request, 'blog/post_list.html', {'posts': posts})

from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
