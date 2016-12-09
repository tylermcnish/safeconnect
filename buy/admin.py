from django.contrib import admin
from .models import Customer
from .models import House
from .models import System
from .models import Receptacle_Installer
from .models import Receptacle_Installer_Availability
from .models import Receptacle_Installation
from .models import House_Availability

# Register your models here.
admin.site.register(Customer)
admin.site.register(House)
admin.site.register(System)
admin.site.register(Receptacle_Installer)
admin.site.register(Receptacle_Installer_Availability)
admin.site.register(Receptacle_Installation)
admin.site.register(House_Availability)