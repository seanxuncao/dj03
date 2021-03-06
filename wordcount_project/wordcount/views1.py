from django.shortcuts import render


def home(request):
    return render(request,"word.html", {"counttext":"100"})

