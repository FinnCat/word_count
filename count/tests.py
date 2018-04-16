from django.test import TestCase

# Create your tests here.
def count_res(text):
    fulltext = text
    word_list = fulltext.split()
    print(word_list)
    word_count = len(word_list)

    word_dic = {}

    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    print(word_dic)

    for word, count_tot in word_dic.items():
        print(word, count_tot)

count_res("Alavilla mailla hallan vaara vaara hallan")
