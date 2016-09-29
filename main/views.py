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
		filename='data/atila.log',
		datefmt='%d-%m-%Y, %H:%M',
		level=logging.INFO)

c = configparser.ConfigParser()
c.read("data/auth.ini")

admin = c.get('mail','admin')
fromaddr = c.get('mail','fromaddr')

client = pm.MongoClient(c.get('db','host'), int(c.get('db','port')))

atdb = client[c.get('db','db')]

if os.uname()[1][:9] != "applejack":
	atdb.authenticate(c.get('db','user'), c.get('db','pass'))

coll = atdb[c.get('db','coll')] 


def get_client_ip(request):
	ip = request.META.get('HTTP_CF_CONNECTING_IP')
	if ip is None:
		ip = request.META.get('REMOTE_ADDR')
	return ip


class Home(View):

	def get(self, request):

		underconst = False

		programDay1 = p.programDay1
		programDay2 = p.programDay2

		clips = list(coll.find({'affiliation':'CLiPS'}, {'name':1,'_id':0}))
		ticc = list(coll.find({'affiliation':'TiCC'}, {'name':1,'_id':0}))
		lt3 = list(coll.find({'affiliation':'LT3'}, {'name':1,'_id':0}))
		lama = list(coll.find({'affiliation':'LaMa'}, {'name':1,'_id':0}))

		if(underconst is False):
			return render(request, 'video-background.html', {
				'programDay1':programDay1,
				'programDay2':programDay2,
				'clips':clips,
				'ticc':ticc,
				'lt3':lt3,
				'lama':lama,
			})
		else:
			return render(request, 'under_construction.html', {
			})


	def post(self, request):


		if "register" in request.POST:				

			name = request.POST['name']
			email = request.POST['email']
			affiliation = request.POST['affiliation']

			events = request.POST.getlist('events')

			diet = request.POST['diet']

			if(diet==''):
				diet = 'N/A'

			hotel = request.POST['hotel']
			room = request.POST['room']	
			roommate = request.POST['roommate']			

			info = {'name':name,'email':email,'affiliation':affiliation, 'diet':diet,'hotel':hotel,'room':room, 'roommate':roommate}

			if(list(coll.find({'email':email}))):

				programDay1 = p.programDay1
				programDay2 = p.programDay2
				clips = list(coll.find({'affiliation':'CLiPS'}, {'name':1,'_id':0}))
				ticc = list(coll.find({'affiliation':'TiCC'}, {'name':1,'_id':0}))
				lt3 = list(coll.find({'affiliation':'LT3'}, {'name':1,'_id':0}))
				lama = list(coll.find({'affiliation':'LaMa'}, {'name':1,'_id':0}))

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

				coll.insert(info)

				msg = p.registration_email_msg + '\n\nName: ' + name + '\nEmail: ' + email + '\nAffiliation: ' +  affiliation +\
												 '\nEvents that you have applied: ' + eventsstr +\
												 '\nDiet Restrictions: ' + diet + '\nHotel: ' + hotel + '\nRoom Preference: ' + room +\
												 '\nRoommate' + roommate
												 

				send_mail(p.registration_email_sbj, msg, fromaddr, [admin])
				send_mail(p.registration_email_sbj, msg, fromaddr, [email])


				if(affiliation=='LaMa'):

					return HttpResponseRedirect('http://applejack.science.ru.nl/atila2016/')

				elif(affiliation=='Other'):

					send_mail(p.registration_email_sbj, msg, fromaddr, [c.get('mail','iris')])

					return HttpResponseRedirect('http://applejack.science.ru.nl/atila2016/')

				elif(affiliation in ['CLiPS','TiCC','LT3']):

					return HttpResponseRedirect('https://fdl-ru.paydro.com/atila-2016')

				else:

					return HttpResponseRedirect('http://applejack.science.ru.nl/atila2016/')


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

					dalist = list(coll.find().sort('affiliation',1))
	
					totalCount = coll.find().count()
					day1Count = coll.find({'Day1':'Yes'}).count()
					day2Count = coll.find({'Day2':'Yes'}).count()
					dinnerCount = coll.find({'Dinner':'Yes'}).count()
					hotelCount = coll.find({'hotel':'Yes'}).count()
					singleCount = coll.find({'room':'Single'}).count()
					doubleCount = coll.find({'room':'Double'}).count()

					return render(request, 'displaydata.html', {
							'askpass': False,
							'dalist': dalist,
							'totalCount':totalCount,
							'day1Count':day1Count,
							'day2Count':day2Count,
							'dinnerCount':dinnerCount,
							'hotelCount':hotelCount,
							'singleCount':singleCount,
							'doubleCount':doubleCount,
					})

				else:

					return render(request, 'displaydata.html', {	
							'askpass': True,
							'warning': 'Invalid password, please try again.',
					})




