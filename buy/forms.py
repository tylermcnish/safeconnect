from django import forms
from django.forms import ModelForm
from .models import House
from .models import House_Availability
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
from django.utils.translation import ugettext_lazy as _


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

class House_Availability_Form(forms.ModelForm):
    class Meta:
        model = House_Availability
        fields = ('available_date',)
        widgets = {
            'available_date': forms.DateInput(attrs={'id': 'datepicker'}),
            }
        labels = {
            'available_date': _('')
        }