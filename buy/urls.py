from django.conf.urls import url
from django.conf import settings
from django.conf.urls import patterns
from . import views

urlpatterns = [
               url(r'^address',views.address,name='address'),
                url(r'^address2',views.address2,name='address2'),
               url(r'^electricity',views.electricity,name='electricity'),
               url(r'^roof$',views.roof,name='roof'),
               url(r'^electrical',views.electrical,name='electrical'),
               url(r'^installation',views.installation,name='installation'),
               url(r'^roof_installation',views.roof_installation,name='roof_installation'),
               url(r'^appliance_installation',views.appliance_installation,name='appliance_installation'),
               url(r'^purchase',views.purchase,name='purchase'),
               url(r'^index',views.index,name='index'),
               url(r'^$',views.index,name='index')
               ]

if settings.DEBUG:
    #static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))  
        