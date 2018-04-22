from django.shortcuts import render, HttpResponse

from .models import Blog

# Create your views here.
def list_blogs(request):
    return HttpResponse('Tämä on list_blog -view funktio, taustalla hyrrää PostgreSQL 10')


def home_blog(request):
    blogs = Blog.objects
    return render(request, 'base.html', {'blogs':blogs})