from django.urls import path

from .views import list_blogs, home_blog

urlpatterns = [
    path('', list_blogs, name='blog_list'),
    path('home/', home_blog, name='blog_home'),

]