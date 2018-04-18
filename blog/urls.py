from django.urls import path

from .views import list_blogs

urlpatterns = [
    path('', list_blogs, name='blog_list'),

]