from django.urls import path

from .views import count_words, count_res, about

urlpatterns = [
    path('', count_words, name='word_count'),
    path('res/', count_res, name='name_res_count'),
    path('about/', about, name='about'),
]