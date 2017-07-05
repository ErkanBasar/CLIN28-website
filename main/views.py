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


def get_client_ip(request):
	ip = request.META.get('HTTP_CF_CONNECTING_IP')
	if ip is None:
		ip = request.META.get('REMOTE_ADDR')
	return ip

# Not in use;
def check_email(request):
	response = {}
	if(participants_collection.find_one({'email': request.GET['email']})):
		response['exists'] = True
	else:
		response['exists'] = False
	return HttpResponse(json.dumps(response), content_type="application/json")

class Home(View):

	program = sorted(list(program_collection.find()), key=lambda k: k['time'])
	for session in program:
		if('slots' in session):
			session['slots'] = sorted(session['slots'], key=lambda k: k['time'])
	organization_team = list(organization_collection.find())[0]['team']

	template = 'base.html'

	def get(self, request):

#		Uncomment to display under construction page.
#		if(os.uname()[1][:9] == 'applejack'):
#			return render(request, 'under_construction.html', {})
#		else:

			return render(request, self.template, {
				'program': self.program,
				'organization_team': self.organization_team,
			})

	def post(self, request):

		if "register" in request.POST:

			registeration_info = {
					'name': request.POST['name'],
					'email': request.POST['email'],
					'registration_time': datetime.now()
			}

			participants_collection.insert(registeration_info)

			msg = p.registration_email_msg + '\n\nName: ' + registeration_info['name'] + '\nEmail: ' + registeration_info['email'] + '\n\n'

			send_mail(p.registration_email_sbj, msg, settings.EMAIL_HOST_USER, [registeration_info['email']])

			return HttpResponseRedirect('http://clin28.cls.ru.nl')


class Dates(View):

	organization_team = list(organization_collection.find())[0]['team']
	template = 'dates.html'

	def get(self, request):

		dates_list = list(dates_collection.find().sort('order',1))

		return render(request, self.template, {
			'organization_team': self.organization_team,
			'dates_list': dates_list,
		})


class Calls(View):

	organization_team = list(organization_collection.find())[0]['team']
	template = 'calls.html'

	def get(self, request):

		return render(request, self.template, {
			'organization_team': self.organization_team,
		})


class DisplayParticipants(View):

	template = 'display_participants.html'

	def get(self, request):

		client_address = get_client_ip(request)

		logging.info('Request to display data page : ' + client_address)

		participant_list = list(participants_collection.find().sort('registration_time',1))

		counts = {}
		counts['total'] = participants_collection.find().count()

		return render(request, self.template, {
			'participant_list': participant_list,
			'counts': counts,
		})
