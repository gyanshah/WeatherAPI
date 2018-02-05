"""from django.shortcuts import render
from django.views.generic.base import TemplateView
from weather import Weather

# Create your views here.

class HomeView(TemplateView):
	template_name="home.html"
	def get(self,request,*args,**kwargs):
		context=self.get_context_data(**kwargs)
		weather=Weather()
		location=weather.lookup_by_location('halifax')
		condition=location.condition()
		context['condition']=condition
		return self.render_to_response(context)"""
from .forms import WeatherForm
from django.views.generic.edit import FormView
from weather import Weather

class WeatherFormView(FormView):
	template_name='form.html'
	form_class=WeatherForm

	def post(self,request,*args,**kwargs):
		context=self.get_context_data(**kwargs)
		city=request.POST.get('city',None)
		woeid=request.POST.get('woeid',None)	
		weather=Weather()
		condition={}
		if city:
			try:
				location=weather.lookup_by_location(city)
				condition=location.condition()
			except:
				pass
		elif woeid:
			try:
				lookup=weather.lookup(woeid)
				condition=location.condition()
			except:
				pass
		date=condition.get('date')
		temp=condition.get('temp')
		status=condition.get('text')

		context['date']=date
		context['temp']=temp
		context['status']=status
	
		return self.render_to_response(context)
