from django.shortcuts import render, HttpResponse


def timeline(request):
    return render(request, 'timeline.html')

def about(request):
        return render(request, 'about_me.html')