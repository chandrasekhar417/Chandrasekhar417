from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fullname = request.GET['fullname']
    wordlist = fullname.split()

    wordis = ''
    count = 0
    for word in wordlist:
        if len(word) > count:
            count = len(word)
            wordis = word

    return render(request, 'count.html', {'finalword' : wordis, 'count' : count, 'fullname' : fullname})
