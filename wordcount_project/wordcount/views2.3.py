from django.shortcuts import render


def home(request):
    return render(request,"word.html", {"counttext":"100"})

def countword(request):
    words = request.GET['fulltext']
    wordlist = words.split(" ")
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    return render(request,"count.html", {"words":words, "worddict":worddict,"len": len(wordlist)})

