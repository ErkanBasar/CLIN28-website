from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse

from django.conf import settings

import os
import json
import logging
import pymongo as pm
import configparser
from datetime import datetime

import program as p

logging.basicConfig(
        format='%(asctime)s, %(levelname)s: %(message)s',
        filename='data/clin28.log',
        datefmt='%d-%m-%Y, %H:%M',
        level=logging.INFO)

c = configparser.ConfigParser()
c.read("data/auth.ini")

client = pm.MongoClient(c.get('db','host'), int(c.get('db','port')))
clindb = client[c.get('db','db')]

if os.uname()[1][:9] != "applejack":
    clindb.authenticate(c.get('db','user'), c.get('db','pass'))

program_collection = clindb[c.get('db','program_collection')]
participants_collection = clindb[c.get('db','participants_collection')]
organization_collection = clindb[c.get('db','organization_collection')]
dates_collection = clindb[c.get('db','dates_collection')]

class Home(View):

    def get(self, request):

#        Uncomment to display under construction page.
#        if(os.uname()[1][:9] == 'applejack'):
#            return render(request, 'under_construction.html', {})
#        else:

            program = sorted(list(program_collection.find()), key=lambda k: k['time'])
            for session in program:
                if('slots' in session):
                    session['slots'] = sorted(session['slots'], key=lambda k: k['time'])

            organization_team = list(organization_collection.find())[0]['team']

            return render(request, 'base.html', {
                'program': self.program,
                'organization_team': self.organization_team,
            })

class Dates(View):

    def get(self, request):

        organization_team = list(organization_collection.find())[0]['team']
        dates_list = list(dates_collection.find().sort('order',1))

        return render(request, 'dates.html', {
            'organization_team': organization_team,
            'dates_list': dates_list,
        })

class Calls(View):

    def get(self, request):

        organization_team = list(organization_collection.find())[0]['team']

        return render(request, 'calls.html', {
            'organization_team': organization_team,
        })

class SharedTask(View):

    def get(self, request):

        organization_team = list(organization_collection.find())[0]['team']
        dates = dates_collection.find({'title' : 'Shared task: Spelling correction'})[0]

        return render(request, 'shared_task.html', {
            'organization_team': organization_team,
            'dates': dates,
        })

class ThesisPrize(View):

    def get(self, request):

        organization_team = list(organization_collection.find())[0]['team']

        return render(request, 'stil_thesis_prize.html', {
            'organization_team': organization_team,
        })
