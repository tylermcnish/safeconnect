from django import forms
from django.forms import ModelForm
from .models import House


class House_Form(forms.ModelForm):
    class Meta:
        model = House
        fields = ('address',)

class Electricity_Form(forms.ModelForm):
    class Meta:
        model = House
        fields = ('monthly_electricity_usage','your_current_electricity_provider')

class Roof_Form(forms.ModelForm):
    class Meta:
        model = House
        fields = ('stories','roof_type')

class Electrical_Service_Form(forms.ModelForm):
    class Meta:
        model = House
        fields = ('main_breaker_size','busbar_capacity','is_there_room_for_new_breaker_opposite_main_breaker',)