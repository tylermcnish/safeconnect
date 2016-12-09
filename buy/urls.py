from django.conf.urls import url
from django.conf import settings
from django.conf.urls import patterns
from . import views

urlpatterns = [
               url(r'^address',views.address,name='address'),
               url(r'^electricity',views.electricity,name='electricity'),
               url(r'^roof',views.roof,name='roof'),
               url(r'^electrical',views.electrical,name='electrical'),
               #url(r'^system',views.system,name='system'),
               url(r'^installation',views.installation,name='installation'),
               url(r'^index',views.index,name='index'),
               url(r'^$',views.index,name='index')
               ]

if settings.DEBUG:
    #static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))  
        