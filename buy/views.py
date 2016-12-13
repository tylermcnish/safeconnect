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
from .models import Appliance
from .models import Roof_Installer
from .models import Roof_Installer_Availability
from .models import Appliance_Installer
from .models import Appliance_Installer_Availability
from decimal import Decimal


# Create your views here.



def index(request):
    return render(request, 'buy/index.html',{}) 

def address(request):
    #define variables
    links=[["Address > ","#address", "page-scroll"], ["Electric Bill > ","#electricity", "disabled"], ["Roof > ","#roof", "disabled"], ["House Electrical >","#electrical", "disabled"], ["Financing >","/financing", "disabled"], ["Installation >","/installation", "disabled"], ["Purchase!","/purchase", "disabled"]]
    section_id="address"
    form = House_Form()
    heading="Design your Appliance"
    subheading="With a few pieces of information, SafeConnect can recommend an appliance size and roof peg type that will work for your house and matches your electricity needs. To get started, enter your address."
    img_url=""
    action="address2"
    note=""
    context = {'form':form, 'links':links, 'heading':heading, 'subheading':subheading, 'note':note, 'img_url':img_url,'action':action, 'section_id':section_id}
    #if this view is called via a form, post, process the form data as set forth in this if statement.
    if request.method == 'POST':
        form = House_Form(request.POST)
        if form.is_valid():
            #put new house and calculated max roof capacity in database
            instance=form.save(commit=False)
            instance.max_roof_capacity=instance.roof_area/1.5*.240
            instance.max_roof_production=instance.max_roof_capacity*.18*365*24
            instance.save()
            #pass new house record to next view using middleware
            a = instance.pk
            request.session['pass_house'] = a
            #call the "address2" view 
            return address2(request)
    #if request method is not post, that means its first view of this page, so just render the design template using the variables set forth in this view.
    else: 
        return render(request,'buy/design.html',context)
    
def address2(request):        
    #receive address entered on previous page via middleware, and pass it right back to middleware, because it's not used on this view but needs to be passed to next view.
    a = request.session.get('pass_house')
    instance=House.objects.get(pk=a)
    request.session['pass_house'] = a
    #re-set variables
    section_id="address2"
    links=[["Address > ","#address", "page-scroll"], ["Electric Bill > ","#electricity", "disabled"], ["Roof > ","#roof", "disabled"], ["House Electrical >","#electrical", "disabled"], ["Financing >","/financing", "disabled"], ["Installation >","/installation", "disabled"], ["Purchase!","/purchase", "disabled"]]
    form = ""
    heading="Confirm your Location"
    subheading="Please position the pointer on your roof."
    note="[Note: this section is not yet functional, but would be the Project SunRoof or Geostellar functionality that would (1) use a 3D model of the customer's roof and shading to generate a max system size and (2) use an insolation database to estimate system production.  Can we can really do (1) without an on-site visit?  Even if so, do we at need an online system that allows the customer to position the modules on the roof?  If so, will customers really buy solar this way?]"
    img_url="img/project_sunroof.png"
    action="electricity"
    context = {'form':form, 'links':links, 'heading':heading, 'subheading':subheading, 'note':note, 'img_url':img_url,'action':action, 'section_id':section_id, 'address':instance.address}
    #render the design page using the new variables set forth in this view.
    return render(request,'buy/design.html',context)

def electricity(request):
    #receive address from middleware
    a = request.session.get('pass_house')
    instance=House.objects.get(pk=a)
    #set variables
    section_id="electricity"
    links=[["Address > ","/address", "page-scroll"], ["Electric Bill > ","#electricity", "page-scroll"], ["Roof > ","#roof", "disabled"], ["House Electrical >","#electrical", "disabled"], ["Financing >","/financing", "disabled"], ["Installation >","/installation", "disabled"], ["Purchase!","/purchase", "disabled"]]
    form = Electricity_Form()
    heading="Your Electric Bill"
    subheading="Find the amount of electricity you use per month on your electric bill and enter it below.  This should be an amount measured in kWh.  If your bill presents an average, please use that for the best accuracy.  Alternatively, you can average your last few electric bills and enter the average."    
    img_url="img/energy_bill.png"
    action="electricity"
    note=""
    context = {'form':form, 'links':links, 'heading':heading, 'subheading':subheading, 'note':note, 'img_url':img_url,'action':action, 'section_id':section_id, 'address':instance.address, 'insolation':instance.insolation, 'roof_area':instance.roof_area, 'max_roof_capacity':instance.max_roof_capacity, 'max_roof_production':instance.max_roof_production, 'address':instance.address}
    #if page was called from form post, save form data to database for instance record.
    if request.method == 'POST':
        form = Electricity_Form(request.POST, instance=instance)
        if form.is_valid():
            form.save(commit=False)
            instance.desired_system_capacity=(int(instance.monthly_electricity_usage)*12)/(.18*365*24)
            form.save()
            request.session['pass_house'] = a
            return roof(request)
        #this statement gets triggered on first trip through this view, because the view was called from a "post" by previous page, but the form on this page is not yet valid
        else:
            return render(request,'buy/design.html', context)
    #this statement gets triggered if you navigate to this page from external, as in use of breadcrumb nav when you've already progressed to a further form.
    else:
        return render(request,'buy/design.html', context)

#the roof and electrical service views work like the above views--see notes above.

def roof(request):
    a = request.session.get('pass_house')
    instance=House.objects.get(pk=a)
    section_id="roof"
    links=[["Address > ","/address", "page-scroll"], ["Electric Bill > ","/electricity", "page-scroll"], ["Roof > ","#roof", "page-scroll"], ["House Electrical >","#electrical", "disabled"], ["Financing >","/financing", "disabled"], ["Installation >","/installation", "disabled"], ["Purchase!","/purchase", "disabled"]]
    form = Roof_Form()
    heading="About Your Roof"
    subheading="In order to provide the right roof attachments to your roofing contractors and size your SmartCable, we need to know the approximate height of your roof and the style of your roof."    
    img_url=""
    action="roof"
    note=""
    context = {'form':form, 'links':links, 'heading':heading, 'subheading':subheading, 'note':note, 'img_url':img_url,'action':action, 'section_id':section_id,'address':instance.address, 'insolation':instance.insolation, 'roof_area':instance.roof_area, 'max_roof_capacity':instance.max_roof_capacity, 'max_roof_production':instance.max_roof_production, 'monthly_electricity_usage':instance.monthly_electricity_usage, 'desired_system_capacity':instance.desired_system_capacity}
    if request.method == 'POST':
        form = Roof_Form(request.POST, instance=instance)
        if form.is_valid():
            form.save(commit=False)
            instance.cable_length=instance.stories*10+15
            form.save()
            request.session['pass_house'] = a
            return electrical(request)
        else:
            return render(request,'buy/design.html', context)
    else:
        return render(request,'buy/design.html', context)

def electrical(request):
    a = request.session.get('pass_house')
    instance=House.objects.get(pk=a)
    section_id="electrical"
    links=[["Address > ","/address", "page-scroll"], ["Electric Bill > ","/electricity", "page-scroll"], ["Roof > ","/roof", "page-scroll"], ["House Electrical >","#electrical", "page-scroll"], ["Financing >","/financing", "disabled"], ["Installation >","/installation", "disabled"], ["Purchase!","/purchase", "disabled"]]
    heading="Your Electrical System"
    subheading="In order to make sure your house's electrical system is solar-ready, we need some information about your home's load center (also known as a main panel).  Your load center will likely be located in your basement, garage, or utility room, and will look something like the picture below."    
    img_url="img/load_center.png"
    action="electrical"
    note=""
    form=Electrical_Service_Form()
    context = {'form':form, 'links':links, 'heading':heading, 'subheading':subheading, 'note':note, 'img_url':img_url,'action':action, 'section_id':section_id, 'address':instance.address, 'insolation':instance.insolation, 'roof_area':instance.roof_area, 'max_roof_capacity':instance.max_roof_capacity, 'max_roof_production':instance.max_roof_production, 'monthly_electricity_usage':instance.monthly_electricity_usage, 'desired_system_capacity':instance.desired_system_capacity, 'roof_type':instance.roof_type, 'cable_length':instance.cable_length}
    if request.method == 'POST':
        form = Electrical_Service_Form(request.POST, instance=instance)
        if form.is_valid():
            form.save(commit=False)
            if instance.is_there_room_for_new_breaker_opposite_main_breaker == 'Yes':
                breaker_factor=1
            else:
                breaker_factor=0
            method1=(instance.busbar_capacity-instance.main_breaker_size)/1.25
            method2=int(breaker_factor)*(instance.busbar_capacity*1.2-instance.main_breaker_size)/1.25
            instance.max_electrical_system_capacity_amps=max(method1, method2)
            instance.max_electrical_system_capacity_kW=instance.max_electrical_system_capacity_amps*240/1000
            form.save()
            #calc values that will be saved as new appliance record
            system_capacity=Decimal(min(instance.desired_system_capacity, instance.max_roof_capacity, instance.max_electrical_system_capacity_kW, 7.68))
            number_of_modules=int(system_capacity/Decimal(.240))
            system_value=system_capacity*1000*1+2000
            system_production=system_capacity*Decimal(.18)*Decimal(365)*Decimal(24)
            percent_of_electric_bill=system_production/(int(instance.monthly_electricity_usage)*12)*100
            if system_capacity>3.85:
                smartbox_size=40
            else:
                smartbox_size=20
            new_appliance=Appliance(house=instance, system_capacity=system_capacity, number_of_modules=number_of_modules, system_value=system_value, system_production=system_production, percent_of_electric_bill=percent_of_electric_bill, smartbox_size=smartbox_size)
            new_appliance.save()
            request.session['pass_appliance'] = new_appliance.pk
            context = {'address':instance.address, 'insolation':instance.insolation, 'roof_area':instance.roof_area, 'max_roof_capacity':instance.max_roof_capacity, 'max_roof_production':instance.max_roof_production, 'monthly_electricity_usage':instance.monthly_electricity_usage, 'desired_system_capacity':instance.desired_system_capacity, 'roof_type':instance.roof_type, 'cable_length':instance.cable_length,'max_electrical_system_capacity_kW':instance.max_electrical_system_capacity_kW,'system_capacity':system_capacity, 'smartbox_size': smartbox_size, 'number_of_modules': number_of_modules, 'system_value': system_value, 'system_production': system_production, 'percent_of_electric_bill':percent_of_electric_bill}
            #now just render staic system page -- no forms on page currently.
            return render(request,'buy/system.html',context)
        else:
            return render(request,'buy/design.html', context)
    else:
        return render(request,'buy/design.html', context)

def installation(request):
    #set variables
    house_availability_form = House_Availability_Form(request.POST)
    a = request.session.get('pass_appliance')
    instance=Appliance.objects.get(pk=a)
    header_text="Schedule PV Plug Installation"
    text="Select a date to see SafeConnect electrician partners available to install your PV Plug."
    note="[Note: Try 12/20/16 and 12/21/16.]"
    action="installation"
    button_name="receptacle_installer"
    img_source=""
    if request.method == 'POST':
        #this is triggered if a list of installers has been generated and one has been selected by user.
        if 'receptacle_installer' in request.POST:
            y=request.POST.get('receptacle_installer')
            n=Receptacle_Installer.objects.get(pk=y)
            instance.receptacle_installer=n
            instance.save()
            request.session['pass_appliance'] = a
            return roof_installation(request)
        #this is triggered when house picker is used, and list of installers not yet generated
        elif house_availability_form.is_valid():
            #save the selected date to the appliance database -can be changed later on reselect
            x=request.POST.get('available_date')
            instance.receptacle_installation_date=x
            instance.save()
            #generate list of available installers
            installer_list=Receptacle_Installer.objects.filter(receptacle_installer_availability__available_date=x)
            #re-render the installation page with list of available installers
            context = {'house_availability_form':house_availability_form, 'installer_list':installer_list, 'text':text, 'header_text': header_text, 'action':action, 'note':note, 'button_name':button_name, 'img_source':img_source}
            return render(request,'buy/installation.html',context) 
        #not sure when this is triggered
        else:
            context = {'house_availability_form':house_availability_form, 'text':text, 'header_text': header_text, 'action':action, 'note':note}
            return render(request,'buy/installation.html',context)
    #this is triggered when page first viewed and no date yet selected.        
    else:
        text="Select a date to see SafeConnect electrician partners available to install your PV Plug."
        context = {'house_availability_form':house_availability_form, 'text':text, 'header_text': header_text, 'action':action, 'note':note}
        return render(request,'buy/installation.html',context)
    
#Once you have the form submission for the installer figured out, make separate similar views for next two forms, using same template.  Need to build databases and forms.

def roof_installation(request):
    house_availability_form=House_Availability_Form(request.POST)
    header_text="Schedule Roof Mount Installation"
    text="Select a date to see SafeConnect roofer partners available to install your PV Plug."
    action="roof_installation"
    note=""
    href=""
    button_name="roof_installer"
    a = request.session.get('pass_appliance')
    instance=Appliance.objects.get(pk=a)
    if request.method == 'POST':
        #this is triggered if a list of installers has been generated and one has been selected by user.
        if 'roof_installer' in request.POST:
            y=request.POST.get('roof_installer')
            n=Roof_Installer.objects.get(pk=y)
            instance.roof_installer=n
            instance.save()
            request.session['pass_appliance'] = a
            return appliance_installation(request)
        #this is triggered when house picker is used, and list of installers not yet generated
        elif house_availability_form.is_valid():
            x=request.POST.get('available_date')
            #generate list of available installers
            installer_list=Roof_Installer.objects.filter(roof_installer_availability__available_date=x)
            #save the selected date to the appliance database -can be changed later on reselect
            instance.roof_installation_date=x
            instance.save()
            #re-render the installation page with list of available installers
            context = {'house_availability_form':house_availability_form, 'installer_list':installer_list, 'text':text, 'header_text': header_text, 'action':action, 'note':note, 'button_name':button_name}
            return render(request,'buy/installation.html',context) 
    #not sure when this is triggered
        else:
            context = {'house_availability_form':house_availability_form, 'text':text, 'header_text': header_text, 'action':action, 'note':note, 'href':href}
            return render(request,'buy/installation.html',context)
    else:
        context = {'house_availability_form':house_availability_form, 'text':text, 'header_text': header_text, 'action':action, 'note':note, 'href':href}
        return render(request,'buy/installation.html',context)

def appliance_installation(request):
    house_availability_form=House_Availability_Form(request.POST)
    header_text="Schedule Appliance Installation"
    text="Select a date to see SafeConnect appliance partners available to install your appliance."
    action="appliance_installation"
    note=""
    href=""
    button_name="appliance_installer"
    a = request.session.get('pass_appliance')
    instance=Appliance.objects.get(pk=a)
    if request.method == 'POST':
        #this is triggered if a list of installers has been generated and one has been selected by user.
        if 'appliance_installer' in request.POST:
            y=request.POST.get('appliance_installer')
            n=Appliance_Installer.objects.get(pk=y)
            instance.appliance_installer=n
            instance.save()
            return purchase(request)
        #this is triggered when house picker is used, and list of installers not yet generated
        elif house_availability_form.is_valid():
            x=request.POST.get('available_date')
            #generate list of available installers
            installer_list=Appliance_Installer.objects.filter(appliance_installer_availability__available_date=x)
            #save the selected date to the appliance database -can be changed later on reselect
            instance.appliance_installation_date=x
            instance.save()
            #re-render the installation page with list of available installers
            context = {'house_availability_form':house_availability_form, 'installer_list':installer_list, 'text':text, 'header_text': header_text, 'action':action, 'note':note, 'button_name':button_name}
            return render(request,'buy/installation.html',context) 
    #not sure when this is triggered
        else:
            context = {'house_availability_form':house_availability_form, 'text':text, 'header_text': header_text, 'action':action, 'note':note, 'href':href}
            return render(request,'buy/installation.html',context)
    else:
        context = {'house_availability_form':house_availability_form, 'text':text, 'header_text': header_text, 'action':action, 'note':note, 'href':href}
        return render(request,'buy/installation.html',context)

def purchase(request):
    return render(request,'buy/purchase.html')