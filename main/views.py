from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail

import os
import pymongo as pm
import configparser

import program as p

c = configparser.ConfigParser()
c.read("data/auth.ini")

admin = c.get('mail','admin')
fromaddr = c.get('mail','fromaddr')

client = pm.MongoClient(c.get('db','host'), int(c.get('db','port')))

atdb = client[c.get('db','db')]

if os.uname()[1][:9] != "applejack":
	atdb.authenticate(c.get('db','user'), c.get('db','pass'))

coll = atdb[c.get('db','coll')] 


class Home(View):

	def get(self, request):

		underconst = False

		programDay1 = p.programDay1
		programDay2 = p.programDay2

		clips = list(coll.find({'affiliation':'clips'}, {'name':1,'_id':0}))
		ticc = list(coll.find({'affiliation':'ticc'}, {'name':1,'_id':0}))
		lt3 = list(coll.find({'affiliation':'lt3'}, {'name':1,'_id':0}))
		lama = list(coll.find({'affiliation':'lama'}, {'name':1,'_id':0}))

		print(lama)

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

			programDay1 = p.programDay1
			programDay2 = p.programDay2
			clips = list(coll.find({'affiliation':'clips'}, {'name':1,'_id':0}))
			ticc = list(coll.find({'affiliation':'ticc'}, {'name':1,'_id':0}))
			lt3 = list(coll.find({'affiliation':'lt3'}, {'name':1,'_id':0}))
			lama = list(coll.find({'affiliation':'lama'}, {'name':1,'_id':0}))


			name = request.POST['name']
			email = request.POST['email']
			affiliation = request.POST['affiliation']

			events = request.POST.getlist('events')

			diet = request.POST['diet']

			hotel = request.POST['hotel']
			room = request.POST['room']	
			roommate = request.POST['roommate']			

			info = {'name':name,'email':email,'affiliation':affiliation, 'diet':diet,'hotel':hotel,'room':room, 'roommate':roommate}

			if(list(coll.find({'email':email}))):

				return render(request, 'video-background.html', {
					'emailwarningalert':'True',
					'programDay1':programDay1,
					'programDay2':programDay2,
					'clips':clips,
					'ticc':ticc,
					'lt3':lt3,
					'lama':lama,
				})

			elif(events):
				for e in events:
					info[e] = 'Yes'

				coll.insert(info)

				send_mail(p.registration_email_sbj, p.registration_email_msg, fromaddr, [admin])
				send_mail(p.registration_email_sbj, p.registration_email_msg, fromaddr, [email])

				return render(request, 'video-background.html', {
					'registeralert':'True',
					'programDay1':programDay1,
					'programDay2':programDay2,
					'clips':clips,
					'ticc':ticc,
					'lt3':lt3,
					'lama':lama,
				})

			else:
				return render(request, 'video-background.html', {
					'warningalert':'True',
					'programDay1':programDay1,
					'programDay2':programDay2,
					'clips':clips,
					'ticc':ticc,
					'lt3':lt3,
					'lama':lama,
				})





