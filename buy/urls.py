from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^address',views.address,name='address'),
               url(r'^electricity',views.electricity,name='electricity'),
               url(r'^roof',views.roof,name='roof'),
               url(r'^electrical',views.electrical,name='electrical'),
               url(r'^system',views.system,name='system'),
               url(r'^index',views.index,name='index'),
               url(r'^$',views.index,name='index')
               ]
        