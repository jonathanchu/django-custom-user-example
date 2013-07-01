from django.conf.urls import include, patters, url
from . import views


urlpatters = patterns(
    '',
    url(r'^dashboard/$', views.dashboard, name='accounts_dashboard'),

)
