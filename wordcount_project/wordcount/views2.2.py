from django.shortcuts import render


def home(request):
    return render(request,"word.html", {"counttext":"100"})

def countword(request):
    words = request.GET['fulltext']
    wordlist = words.split(" ")
    return render(request,"count.html", {"words":words, "len": len(wordlist)})

