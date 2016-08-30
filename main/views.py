from django.shortcuts import render
from django.views.generic import View



class Home(View):

	def get(self, request):

		underconst = True

		if(underconst is False):
			return render(request, 'video-background.html', {})
		else:
			return render(request, 'under_construction.html', {})
