from django.contrib import admin
from .models import Customer
from .models import House
from .models import System
from .models import Appliance_Installer

# Register your models here.
admin.site.register(Customer)
admin.site.register(House)
admin.site.register(System)
admin.site.register(Appliance_Installer)