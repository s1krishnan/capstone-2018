from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.venturetrends_home, name='venturetrends_home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/company/it1$', views.it1, name='it1'),
    url(r'^home/company/it2$', views.it2, name='it2'),
    url(r'^home/company/investordetails$', views.investordetails, name='investordetails'),
    url(r'^home/investor/viewmyinvestments', views.viewmyinvestments, name='viewmyinvestments'),
    url(r'^home/investor/comparecompanies$', views.comparecompanies, name='comparecompanies'),
]