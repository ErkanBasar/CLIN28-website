from django.shortcuts import render

from django.conf import settings

def home(request):

    if settings.UNDER_CONST:
        request = render(request, 'under_construction.html', {})
    else:
        request = render(request, 'base.html', {
            'title': 'Computational Linguistics in the Netherlands',
            'keys': 'CLIN28, CLIN 28, Computational Linguistics in the Netherlands, Nijmegen',
        })

    return request

def dates(request):
    return render(request, 'dates.html', {
        'title': 'Important Dates',
        'keys': 'CLIN28, CLIN 28, Important dates',
    })

def calls(request):
    return render(request, 'calls.html', {
        'title': 'Calls',
        'keys': 'CLIN28, CLIN 28, calls, abstracts',
    })

def shared_task(request):
    return render(request, 'shared_task.html', {
        'title': 'Shared task',
        'keys': 'CLIN28, CLIN 28, shared task, shared task call',
    })

def thesis_prize(request):
    return render(request, 'stil_thesis_prize.html', {
        'title': 'Thesis prize',
        'keys': 'CLIN28, CLIN 28, thesis prize, best thesis',
    })

def posters(request):
    return render(request, 'posters.html', {
        'title': 'Gallery',
        'keys': 'CLIN28, CLIN 28, posters, display posters, dowload posters',
    })

def photos(request):
    return render(request, 'photos.html', {
        'title': 'Gallery',
        'keys': 'CLIN28, CLIN 28, photos, photo gallery',
    })
