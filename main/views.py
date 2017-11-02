from django.shortcuts import render
from django.views.generic import View
import logging
import pymongo as pm
import configparser
import os


logging.basicConfig(
    format='%(asctime)s, %(levelname)s: %(message)s',
    filename='data/clin28.log',
    datefmt='%d-%m-%Y, %H:%M',
    level=logging.INFO)

c = configparser.ConfigParser()
c.read("data/auth.ini")

client = pm.MongoClient(c.get('db', 'host'), int(c.get('db', 'port')))
clindb = client[c.get('db', 'db')]

authorized_hosts = ["applejack", "xarou.hom"]
if os.uname()[1][:9] not in authorized_hosts:
    clindb.authenticate(c.get('db', 'user'), c.get('db', 'pass'))

program_collection = clindb[c.get('db', 'program_collection')]
participants_collection = clindb[c.get('db', 'participants_collection')]
organization_collection = clindb[c.get('db', 'organization_collection')]
dates_collection = clindb[c.get('db', 'dates_collection')]

organization_team = []
if list(organization_collection.find()):
    organization_team = list(organization_collection.find())[0]['team']


class Home(View):
    def get(self, request):
        #        Uncomment to display under construction page.
        #        if(os.uname()[1][:9] == 'applejack'):
        #            return render(request, 'under_construction.html', {})

        program = sorted(list(program_collection.find()), key=lambda k: k['time'])
        for session in program:
            if 'slots' in session:
                session['slots'] = sorted(session['slots'], key=lambda k: k['time'])

        return render(request, 'base.html', {
            'title': 'Computational Linguistics in the Netherlands',
            'keys': 'CLIN28, CLIN 28, Computational Linguistics in the Netherlands, Nijmegen',
            'program': program,
            'organization_team': organization_team,
        })


class Dates(View):
    def get(self, request):
        dates_list = list(dates_collection.find().sort('order', 1))

        return render(request, 'dates.html', {
            'title': 'Important Dates',
            'keys': 'CLIN28, CLIN 28, Important dates',
            'organization_team': organization_team,
            'dates_list': dates_list,
        })


class Calls(View):
    def get(self, request):
        return render(request, 'calls.html', {
            'title': 'Calls',
            'keys': 'CLIN28, CLIN 28, calls, abstracts',
            'organization_team': organization_team,
        })


class SharedTask(View):
    def get(self, request):
        dates = dates_collection.find({'title': 'Shared task: Spelling correction'})[0]

        return render(request, 'shared_task.html', {
            'title': 'Shared task',
            'keys': 'CLIN28, CLIN 28, shared task, shared task call',
            'organization_team': organization_team,
            'dates': dates,
        })


class ThesisPrize(View):
    def get(self, request):
        return render(request, 'stil_thesis_prize.html', {
            'title': 'Thesis prize',
            'keys': 'CLIN28, CLIN 28, thesis prize, best thesis',
            'organization_team': organization_team,
        })
