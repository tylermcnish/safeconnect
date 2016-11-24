from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^design',views.design,name='design'),
               url(r'^$',views.index,name='index')
               ]