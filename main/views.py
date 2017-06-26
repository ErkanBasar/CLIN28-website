from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

import os
import logging
import pymongo as pm
import configparser

import program as p

logging.basicConfig(
		format='%(asctime)s, %(levelname)s: %(message)s',
		filename='data/clin28.log',
		datefmt='%d-%m-%Y, %H:%M',
		level=logging.INFO)

c = configparser.ConfigParser()
c.read("data/auth.ini")

admin = c.get('mail','admin')
fromaddr = c.get('mail','fromaddr')

client = pm.MongoClient(c.get('db','host'), int(c.get('db','port')))

clindb = client[c.get('db','db')]

if os.uname()[1][:9] != "applejack":
	clindb.authenticate(c.get('db','user'), c.get('db','pass'))

program_collection = clindb[c.get('db','program_collection')]
participants_collection = clindb[c.get('db','participants_collection')]
organization_collection = clindb[c.get('db','organization_team')]

def get_client_ip(request):
	ip = request.META.get('HTTP_CF_CONNECTING_IP')
	if ip is None:
		ip = request.META.get('REMOTE_ADDR')
	return ip


class Home(View):

	def get(self, request):

#		if(True):
		if(os.uname()[1][:9] == 'applejack'):
			return render(request, 'under_construction.html', {})

		else:

			program = list(program_collection.find())
			# Sort the sesisons by time
			program = sorted(program, key=lambda k: k['time'])

			for session in program:
				if('slots' in session):
					session['slots'] = sorted(session['slots'], key=lambda k: k['time'])

			organization_team = list(organization_collection.find())[0]['team']

			return render(request, 'video-background.html', {
				'program':program,
				'organization_team':organization_team,
			})

	def post(self, request):

		if "register" in request.POST:

			name = request.POST['name']
			email = request.POST['email']

			info = {
					'name':name,
					'email':email,
					'diet':diet,

			}

			# already registered warning
			if(list(participants_collection.find({'email':email}))):

				programDay1 = p.programDay1
				programDay2 = p.programDay2

				return render(request, 'video-background.html', {
					'emailwarningalert':'True',
					'programDay1':programDay1,
					'programDay2':programDay2,
					'clips':clips,
					'ticc':ticc,
					'lt3':lt3,
					'lama':lama,
				})

			else:
				for e in events:
					info[e] = 'Yes'

				eventsstr = ', '.join(events)

				participants_collection.insert(info)

				msg = p.registration_email_msg + '\n\nName: ' + name + '\nEmail: ' + email +\
												 '\nEvents that you have applied: ' + eventsstr +\
												 '\nDiet Restrictions: ' + diet + '\nHotel: ' + hotel + '\nRoom Preference: ' + room +\
												 '\nRoommate: ' + roommate


				send_mail(p.registration_email_sbj, msg, fromaddr, [admin])
				send_mail(p.registration_email_sbj, msg, fromaddr, [email])

				return HttpResponseRedirect('http://clin28.cls.ru.nl')


class ModifyProgram(View):


	def get(self, request):

		return render(request, 'modify_program.html', {
				'askpass': True,
		})

	def post(self, request):

			if "confirmpass" in request.POST:

				user_pass = request.POST['adminpass']

				admin_pass = c.get('admin', 'pass')

				if(user_pass == admin_pass):

					return render(request, 'displaydata.html', {
							'askpass': False,
							'dalist': dalist,
							'counts': counts,
					})

				else:

					return render(request, 'displaydata.html', {
							'askpass': True,
							'warning': 'Invalid password, please try again.',
					})

class DisplayData(View):

	def get(self, request):

		return render(request, 'displaydata.html', {
				'askpass': True,
		})

	def post(self, request):

			if "confirmpass" in request.POST:

				user_pass = request.POST['adminpass']

				admin_pass = c.get('admin', 'pass')

				if(user_pass == admin_pass):

					client_address = get_client_ip(request)

					logging.info('Request to display data page : ' + client_address)

					dalist = list(participants_collection.find().sort('affiliation',1))

					counts = {}
					counts['totalCount'] = participants_collection.find().count()
					counts['day1Count'] = participants_collection.find({'Day1':'Yes'}).count()
					counts['day2Count'] = participants_collection.find({'Day2':'Yes'}).count()
					counts['dinnerCount'] = participants_collection.find({'Dinner':'Yes'}).count()
					counts['hotelCount'] = participants_collection.find({'hotel':'Yes'}).count()
					counts['singleCount'] = participants_collection.find({'room':'Single'}).count()
					counts['doubleCount'] = participants_collection.find({'room':'Double'}).count()

					return render(request, 'displaydata.html', {
							'askpass': False,
							'dalist': dalist,
							'counts': counts,
					})

				else:

					return render(request, 'displaydata.html', {
							'askpass': True,
							'warning': 'Invalid password, please try again.',
					})
