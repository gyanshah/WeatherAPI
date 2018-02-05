from django.conf.urls import *
from .views import WeatherFormView
urlpatterns=[url(r'form/$',WeatherFormView.as_view(),name='form-view'),]

