from django.shortcuts import render
from django.shortcuts import redirect
from .forms import House_Form
from .forms import Electricity_Form
from .forms import Roof_Form
from .forms import Electrical_Service_Form
from .forms import House_Availability_Form
from django.http import HttpResponseRedirect
from .models import House
from .models import House_Availability
from .models import Receptacle_Installer
from .models import Receptacle_Installer_Availability
from decimal import Decimal


# Create your views here.



def index(request):
    return render(request, 'buy/index.html',{})



#ideas: First template - address form only. Second template -- all other forms, submit only on last submit.  Third template -- system with results.

def address(request):
    #if this view is called via a form, post, process the form data as set forth in this if statement.
    if request.method == 'POST':
        house_form = House_Form(request.POST)
        if house_form.is_valid():
            #put new house and calculated max roof capacity in database
            instance=house_form.save(commit=False)
            instance.max_roof_capacity=instance.roof_area/1.5*.240
            instance.max_roof_production=instance.max_roof_capacity*.18*365*24
            instance.save()
            #pass new house record to next view using middleware
            a = instance.address
            request.session['pass_address'] = a
            #render houseforms page
            electricity_form = Electricity_Form()
            context = {'electricity_form':electricity_form, 'address':instance.address, 'insolation':instance.insolation, 'roof_area':instance.roof_area, 'max_roof_capacity':instance.max_roof_capacity, 'max_roof_production':instance.max_roof_production}
            return render(request,'buy/electricity.html', context)
    #if request method is not post, that means its first view of this page, so just need to render house form.
    else:
        house_form = House_Form()
        context = {'house_form':house_form}
        return render(request,'buy/address.html',context)

def electricity(request):
    a = request.session.get('pass_address')
    instance=House.objects.get(address=a)
    electricity_form = Electricity_Form(request.POST, instance=instance)
    if request.method == 'POST':
        if electricity_form.is_valid():
            electricity_form.save(commit=False)
            instance.desired_system_capacity=(int(instance.monthly_electricity_usage)*12)/(.18*365*24)
            electricity_form.save()
            roof_form = Roof_Form()
            context = {'roof_form':roof_form, 'address':instance.address, 'insolation':instance.insolation, 'roof_area':instance.roof_area, 'max_roof_capacity':instance.max_roof_capacity, 'max_roof_production':instance.max_roof_production, 'monthly_electricity_usage:':instance.monthly_electricity_usage, 'desired_system_capacity:':instance.desired_system_capacity}
            request.session['pass_address'] = a
            return render(request,'buy/roof.html',context)
    else:
        context = {'electricity_form':electricity_form, 'address':instance.address}
        return render(request,'buy/electricity.html', context)

def roof(request):
    a = request.session.get('pass_address')
    instance=House.objects.get(address=a)
    roof_form = Roof_Form(request.POST, instance=instance)
    if request.method == 'POST':
        if roof_form.is_valid():
            roof_form.save(commit=False)
            instance.cable_length=instance.stories*10+15
            roof_form.save()
            request.session['pass_address'] = a
            electrical_service_form = Electrical_Service_Form()
            context = {'electrical_service_form':electrical_service_form, 'address':instance.address, 'insolation':instance.insolation, 'roof_area':instance.roof_area, 'max_roof_capacity':instance.max_roof_capacity, 'max_roof_production':instance.max_roof_production, 'monthly_electricity_usage:':instance.monthly_electricity_usage, 'desired_system_capacity:':instance.desired_system_capacity, 'roof_type':instance.roof_type, 'cable_length':instance.cable_length}
            return render(request,'buy/electrical.html',context)
    else:
        context = {'roof_form':roof_form}
        return render(request,'buy/roof.html', context)

def electrical(request):
    a = request.session.get('pass_address')
    instance=House.objects.get(address=a)
    electrical_service_form = Electrical_Service_Form(request.POST, instance=instance)
    if request.method == 'POST':
        if electrical_service_form.is_valid():
            electrical_service_form.save(commit=False)
            if instance.is_there_room_for_new_breaker_opposite_main_breaker == 'Yes':
                breaker_factor=1
            else:
                breaker_factor=0
            method1=(instance.busbar_capacity-instance.main_breaker_size)/1.25
            method2=int(breaker_factor)*(instance.busbar_capacity*1.2-instance.main_breaker_size)/1.25
            instance.max_electrical_system_capacity_amps=max(method1, method2)
            instance.max_electrical_system_capacity_kW=instance.max_electrical_system_capacity_amps*240/1000
            instance.system_capacity=Decimal(min(instance.desired_system_capacity, instance.max_roof_capacity, instance.max_electrical_system_capacity_kW, 7.68))
            instance.number_of_modules=int(instance.system_capacity/Decimal(.240))
            instance.system_value=instance.system_capacity*1000*1+2000
            instance.system_production=instance.system_capacity*Decimal(.18)*Decimal(365)*Decimal(24)
            instance.percent_of_electric_bill=instance.system_production/(int(instance.monthly_electricity_usage)*12)*100
            if instance.system_capacity>3.85:
                instance.smartbox_size=40
            else:
                instance.smartbox_size=20
            request.session['pass_address'] = a
            electrical_service_form.save()
            house_availability_form = House_Availability_Form(request.POST, instance=instance)
            context = {'address':instance.address, 'insolation':instance.insolation, 'roof_area':instance.roof_area, 'max_roof_capacity':instance.max_roof_capacity, 'max_roof_production':instance.max_roof_production, 'monthly_electricity_usage':instance.monthly_electricity_usage, 'desired_system_capacity':instance.desired_system_capacity, 'roof_type':instance.roof_type, 'cable_length':instance.cable_length,'max_electrical_system_capacity_kW':instance.max_electrical_system_capacity_kW,'system_capacity':instance.system_capacity, 'smartbox_size': instance.smartbox_size, 'number_of_modules': instance.number_of_modules, 'system_value': instance.system_value, 'system_production': instance.system_production, 'percent_of_electric_bill':instance.percent_of_electric_bill,}
            return render(request,'buy/system.html',context)
    else:
        context = {'electrical_service_form':electrical_service_form}
        return render(request,'buy/electrical.html',context)

def installation(request):
    #note: I can't get this to validate the data properly and save to the database, but I can use the non-cleaned data (request.Post.get) to populate teh receptacle installer list, which is good enough for mockup now.
    #a = request.session.get('pass_address')
    #instance=House.objects.get(address=a)
    #new_house_availability = House_Availability(name=instance.address, available_date='2016-12-10')
    #print new_house_availability
    #new_house_availability.save()
    house_availability_form = House_Availability_Form(request.POST)
    if request.method == 'POST':
        print request.POST.get('available_date')
        x=request.POST.get('available_date')
        if house_availability_form.is_valid():
            selected_date=house_availability_form.cleaned_data
            receptacle_installer_list=Receptacle_Installer.objects.filter(receptacle_installer_availability__available_date=x)
            #house_availability_form.save()
            context = {'house_availability_form':house_availability_form, 'receptacle_installer_list':receptacle_installer_list}
            return render(request,'buy/installation.html',context)
        else:
            #selected_date=x
            #receptacle_installer_list=Receptacle_Installer.objects.filter(receptacle_installer_availability__available_date=selected_date)
            #print selected_date
            #print receptacle_installer_list
            print 'error'
            print house_availability_form.errors, len(house_availability_form.errors)
            context = {'house_availability_form':house_availability_form, 'receptacle_installer_list':receptacle_installer_list}
            return render(request,'buy/installation.html',context)
            
    else:
        context = {'house_availability_form':house_availability_form}
        return render(request,'buy/installation.html',context)
    
