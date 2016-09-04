from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail

import os
import pymongo as pm
import configparser

c = configparser.ConfigParser()
c.read("data/auth.ini")

client = pm.MongoClient(c.get('db','host'), int(c.get('db','port')))

atdb = client[c.get('db','db')]

if os.uname()[1][:9] != "applejack":
	atdb.authenticate(c.get('db','user'), c.get('db','pass'))

coll = atdb[c.get('db','coll')] 


class Home(View):

	def get(self, request):

		#send_mail('test email', 'hello world', 'relevancerr@gmail.com', ['mustafaerkanbasar@gmail.com'])

		underconst = False

		if(underconst is False):
			return render(request, 'video-background.html', {'registeralert':'False',})
		else:
			return render(request, 'under_construction.html', {'registeralert':'False',})


	def post(self, request):


		if "register" in request.POST:				

			name = request.POST['name']
			email = request.POST['email']
			affiliation = request.POST['affiliation']

			events = request.POST.getlist('events')

			diet = request.POST['diet']

			hotel = request.POST['hotel']
			room = request.POST['room']			

			info = {'name':name,'email':email,'affiliation':affiliation, 'diet':diet,'hotel':hotel,'room':room}

			for e in events:
				info[e] = 'Yes'

			coll.insert(info)

			return render(request, 'video-background.html', {
				'registeralert':'True',
			})





