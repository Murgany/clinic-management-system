from django.shortcuts import render, HttpResponse


def welcome(request):
    return render(request, 'welcome.html')
