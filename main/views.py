from django.shortcuts import render
import logging

logging.basicConfig(
    format='%(asctime)s, %(levelname)s: %(message)s',
    filename='data/clin28.log',
    datefmt='%d-%m-%Y, %H:%M',
    level=logging.INFO)

def home(request):
    # Uncomment to display under construction page.
    # if(os.uname()[1][:9] == 'applejack'):
    #    return render(request, 'under_construction.html', {})
    return render(request, 'base.html', {
        'title': 'Computational Linguistics in the Netherlands',
        'keys': 'CLIN28, CLIN 28, Computational Linguistics in the Netherlands, Nijmegen',
    })

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
