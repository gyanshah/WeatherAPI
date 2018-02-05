from django import forms

class WeatherForm(forms.Form):
	city=forms.CharField(required=False)
	woeid=forms.IntegerField(required=False)
