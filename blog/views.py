from django.shortcuts import render, HttpResponse

# Create your views here.
def list_blogs(request):
    return HttpResponse('Tämä on list_blog -view funktio, taustalla hyrrää PostgreSQL 10')
