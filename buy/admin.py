from django.contrib import admin
from .models import Customer
from .models import House
from .models import Appliance
from .models import Receptacle_Installer
from .models import Receptacle_Installer_Availability
from .models import Roof_Installer
from .models import Roof_Installer_Availability
from .models import Appliance_Installer
from .models import Appliance_Installer_Availability
from .models import House_Availability

# Register your models here.
admin.site.register(Customer)
admin.site.register(House)
admin.site.register(Appliance)
admin.site.register(Receptacle_Installer)
admin.site.register(Receptacle_Installer_Availability)
admin.site.register(Roof_Installer)
admin.site.register(Roof_Installer_Availability)
admin.site.register(Appliance_Installer)
admin.site.register(Appliance_Installer_Availability)
admin.site.register(House_Availability)