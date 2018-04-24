from django.shortcuts import render, get_object_or_404, HttpResponse

from .models import Blog

# Create your views here.
def list_blogs(request):
    return HttpResponse('Tämä on list_blog -view funktio, taustalla hyrrää PostgreSQL 10')


def home_blog(request):
    blogs = Blog.objects
    return render(request, 'base.html', {'blogs':blogs})

def detail_blog(request, blog_id):
    deta_blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog-detail.html', {'dets_blog': deta_blog})