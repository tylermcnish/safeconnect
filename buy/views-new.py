from django.shortcuts import render
from django.shortcuts import redirect
from .forms import House_Form
from .forms import Electricity_Form
from .forms import Roof_Form
from .forms import Electrical_Service_Form
from django.http import HttpResponseRedirect
from .models import House


# Create your views here.



def index(request):
    return render(request, 'buy/index.html',{})

#def design(request):
#    house_form = House_Form()
#    electricity_form = Electricity_Form()
#    context = {'house_form':house_form,'electricity_form':electricity_form}
#    return render(request,'buy/design.html',context)

#ideas: First template - address form only. Second template -- all other forms, submit only on last submit.  Third template -- system with results.

def design(request):
    if request.method == 'POST':
        if house_form.is_valid():
            house_form = House_Form(request.POST)
            a=house_form.cleaned_data['address']
            pass_address = house_form.cleaned_data['address']
            request.session['pass_address'] = pass_address
            return redirect('/design/#address')
    else:
        house_form = House_Form()
        context = {'house_form':house_form,}
        return render(request,'buy/design.html',context)

def design2(request):
    electricity_form = Electricity_Form()
    roof_form = Roof_Form()
    electrical_service_form = Electrical_Service_Form()
        if request.method == 'POST':
            if house_form.is_valid():
                house_form.save()
                #print house_form.cleaned_data['address']
                a=house_form.cleaned_data['address']
                pass_address = house_form.cleaned_data['address']
                request.session['pass_address'] = pass_address
                context = {'house_form':house_form,'electricity_form':electricity_form, 'roof_form':roof_form, 'electrical_service_form':electrical_service_form}
                #return render(request,'buy/design.html',context)
                return redirect('/design/#address')
        elif request.POST.get("monthly_electricity_usage"):
            a = request.session.get('pass_address')
            instance=House.objects.get(address=a)
            electricity_form = Electricity_Form(request.POST, instance=instance)
            roof_form = Roof_Form(request.POST, instance=instance)
            house_form = House_Form()
            electrical_service_form = Electrical_Service_Form(request.POST, instance=instance)
            if electricity_form.is_valid():
                electricity_form.save()
                context = {'house_form':house_form,'electricity_form':electricity_form, 'roof_form':roof_form}
                #print "electricity form used"
                #print instance
                return redirect('/design/#roof')
        elif request.POST.get("roof_type"):
            a = request.session.get('pass_address')
            instance=House.objects.get(address=a)
            roof_form = Roof_Form(request.POST, instance=instance)
            electricity_form = Electricity_Form()
            house_form = House_Form()
            electrical_service_form = Electrical_Service_Form(request.POST, instance=instance)
            if roof_form.is_valid():
                roof_form.save()
                context = {'house_form':house_form,'electricity_form':electricity_form, 'roof_form':roof_form, 'electrical_service_form':electrical_service_form}
                #print "roof form used"
                #print instance
                return redirect('/design/#electricalsystem')
        elif request.POST.get("main_breaker_size"):
            a = request.session.get('pass_address')
            instance=House.objects.get(address=a)
            electrical_service_form = Electrical_Service_Form(request.POST, instance=instance)
            roof_form = Roof_Form(request.POST, instance=instance)
            electricity_form = Electricity_Form(request.POST, instance=instance)
            house_form = House_Form(request.POST, instance=instance)
            if electrical_service_form.is_valid():
                electrical_service_form.save()
                if instance.busbar_capacity-instance.main_breaker_size>39:
                    smartbox_size=40
                else:
                    smartbox_size=20
                print smartbox_size
                context = {'house_form':house_form,'electricity_form':electricity_form, 'roof_form':roof_form, 'electrical_service_form':electrical_service_form, 'smartbox_size': smartbox_size}
                return render(request,'buy/design.html',context)
                #return redirect('/design/#system') This redirect allows me to jump to a position in the template, but if I use this, it will go all the way up and render the thing again with no "post" method, and this will eliminate the variable definition.  Maybe try to do all of the above data entry in a view that doesn't re-render the page.  Then at this point, call a new view that does the calcs and defines the system.
        else:
            print "no form identified"
    else:
        house_form = House_Form()
        electricity_form = Electricity_Form()
        roof_form = Roof_Form()
        electrical_service_form = Electrical_Service_Form()
        context = {'house_form':house_form,'electricity_form':electricity_form, 'roof_form':roof_form, 'electrical_service_form':electrical_service_form,}
        return render(request,'buy/design.html',context)

def design2(request):
    if request.method == 'POST':
        if request.POST.get("address"):
            house_form = House_Form(request.POST)
            electricity_form = Electricity_Form()
            roof_form = Roof_Form()
            electrical_service_form = Electrical_Service_Form()
            if house_form.is_valid():
                house_form.save()
                #print house_form.cleaned_data['address']
                a=house_form.cleaned_data['address']
                pass_address = house_form.cleaned_data['address']
                request.session['pass_address'] = pass_address
                context = {'house_form':house_form,'electricity_form':electricity_form, 'roof_form':roof_form, 'electrical_service_form':electrical_service_form}
                #return render(request,'buy/design.html',context)
                return redirect('/design/#address')
        elif request.POST.get("monthly_electricity_usage"):
            a = request.session.get('pass_address')
            instance=House.objects.get(address=a)
            electricity_form = Electricity_Form(request.POST, instance=instance)
            roof_form = Roof_Form(request.POST, instance=instance)
            house_form = House_Form()
            electrical_service_form = Electrical_Service_Form(request.POST, instance=instance)
            if electricity_form.is_valid():
                electricity_form.save()
                context = {'house_form':house_form,'electricity_form':electricity_form, 'roof_form':roof_form}
                #print "electricity form used"
                #print instance
                return redirect('/design/#roof')
        elif request.POST.get("roof_type"):
            a = request.session.get('pass_address')
            instance=House.objects.get(address=a)
            roof_form = Roof_Form(request.POST, instance=instance)
            electricity_form = Electricity_Form()
            house_form = House_Form()
            electrical_service_form = Electrical_Service_Form(request.POST, instance=instance)
            if roof_form.is_valid():
                roof_form.save()
                context = {'house_form':house_form,'electricity_form':electricity_form, 'roof_form':roof_form, 'electrical_service_form':electrical_service_form}
                #print "roof form used"
                #print instance
                return redirect('/design/#electricalsystem')
        elif request.POST.get("main_breaker_size"):
            a = request.session.get('pass_address')
            instance=House.objects.get(address=a)
            electrical_service_form = Electrical_Service_Form(request.POST, instance=instance)
            roof_form = Roof_Form(request.POST, instance=instance)
            electricity_form = Electricity_Form(request.POST, instance=instance)
            house_form = House_Form(request.POST, instance=instance)
            if electrical_service_form.is_valid():
                electrical_service_form.save()
                if instance.busbar_capacity-instance.main_breaker_size>39:
                    smartbox_size=40
                else:
                    smartbox_size=20
                print smartbox_size
                context = {'house_form':house_form,'electricity_form':electricity_form, 'roof_form':roof_form, 'electrical_service_form':electrical_service_form, 'smartbox_size': smartbox_size}
                return render(request,'buy/design.html',context)
        #return redirect('/design/#system') This redirect allows me to jump to a position in the template, but if I use this, it will go all the way up and render the thing again with no "post" method, and this will eliminate the variable definition.  Maybe try to do all of the above data entry in a view that doesn't re-render the page.  Then at this point, call a new view that does the calcs and defines the system.
        else:
            print "no form identified"
else:
    house_form = House_Form()
        electricity_form = Electricity_Form()
        roof_form = Roof_Form()
        electrical_service_form = Electrical_Service_Form()
        context = {'house_form':house_form,'electricity_form':electricity_form, 'roof_form':roof_form, 'electrical_service_form':electrical_service_form,}
        return render(request,'buy/design.html',context)


#def electricity_form_upload(request):
#    if request.method == 'POST':
#        instance=House.objects.get(pk=1)
#        electricity_form = Electricity_Form(request.POST, instance)
#        if electricity_form.is_valid():
#            electricity_form.save()
#            context = {'electricity_form':electricity_form}
#            return render(request,'buy/design.html',context)
#        else: return errors
#    else:
#        electricity_form = Electricity_Form(instance=instance)
#        context = {'electricity_form':electricity_form}
#        return render(request,'buy/design.html',context)