from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def timeline(request):
    return render(request, 'timeline.html')

def about(request):
        return render(request, 'about_me.html')