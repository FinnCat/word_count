from django.shortcuts import render, HttpResponse
from operator import itemgetter

# Create your views here.

def count_words(request):
    return render(request, 'count-home.html', {"greeting":"No hei, mitäpä kuuluu, lasketaanko sanoja?"})

def count_res(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_count = len(word_list)

    word_dic = {}

    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    sorted_words = sorted(word_dic.items(), key=itemgetter(1), reverse=True)
    # print(type(word_dic))
    return render(request, 'count-res.html', {"words": fulltext, "len_text": word_count, "sortedwords": sorted_words} )

def about(request):
    return render(request, 'about.html')