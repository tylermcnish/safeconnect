from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from datetime import datetime 


class Customer(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Receptacle_Installer(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    about=models.CharField(max_length=1000, default="info about me here")
    price=models.DecimalField(max_digits=9, decimal_places=2, default=750)
    receptacle_installer_pic= models.ImageField(upload_to="")
    def __str__(self):
        return self.name
    
class Receptacle_Installer_Availability(models.Model):
    name=models.ForeignKey(Receptacle_Installer, on_delete=models.CASCADE)
    available_date=models.DateField(blank=True, null=True)
    def __str__(self):
        return self.name.name   

class House(models.Model):
    address=models.CharField(max_length=200)
    insolation=models.DecimalField(max_digits=6, decimal_places=3, default=5)
    roof_area=models.DecimalField(max_digits=6, decimal_places=2, default=100)
    max_roof_capacity=models.DecimalField(max_digits=6, decimal_places=0, default=632)
    max_roof_production=models.DecimalField(max_digits=6, decimal_places=0, default=632)
    monthly_electricity_usage=models.DecimalField(max_digits=6, decimal_places=0, default=632)
    desired_system_capacity=models.DecimalField(max_digits=6, decimal_places=1, default=0)
    PGE='PG&E'
    SF='SF Clean Energy'
    OTHER='Other'
    UTILITY_CHOICES = ((PGE,"PG&E"),(SF,"SF Clean Energy"),(OTHER,"Other"))
    your_current_electricity_provider=models.CharField(max_length=200, choices=UTILITY_CHOICES, default='PGE')
    ASPHALT='Asphalt'
    CORRUGATED='Corrugated'
    TILE='Tile'
    ROOF_CHOICES = ((ASPHALT,"Asphalt"),(CORRUGATED,"Corrugated"),(TILE,"Tile"))
    roof_type=models.CharField(max_length=200, choices=ROOF_CHOICES, default='Asphalt')
    stories=models.IntegerField(default=1)
    cable_length=models.IntegerField(default=0)
    busbar_capacity=models.IntegerField(default=100)
    main_breaker_size=models.IntegerField(default=100)
    YES='Yes'
    NO='No'
    IDK='Help me figure it out'
    ROOM_CHOICES = ((YES,"Yes"),(NO,"No"),(IDK,"Help me figure it out"))
    is_there_room_for_new_breaker_opposite_main_breaker=models.CharField(max_length=200, choices=ROOM_CHOICES, default="Yes")
    max_electrical_system_capacity_amps=models.DecimalField(max_digits=6, decimal_places=0, default=0)
    max_electrical_system_capacity_kW=models.DecimalField(max_digits=6, decimal_places=0, default=0)
    system_capacity=models.DecimalField(max_digits=6, decimal_places=0, default=0)
    number_of_modules=models.IntegerField(default=0)
    smartbox_size=models.IntegerField(default=0)
    system_value=models.DecimalField(max_digits=8, decimal_places=2, default=0)
    system_production=models.DecimalField(max_digits=6, decimal_places=0, default=0)
    percent_of_electric_bill=models.DecimalField(max_digits=6, decimal_places=0, default=0)
    receptacle_installer=models.ForeignKey(Receptacle_Installer, on_delete=models.CASCADE, null=True, blank=True)
    receptacle_installation_date=models.DateField(blank=True, null=True)
    def __str__(self):
        return self.address

class House_Availability(models.Model):
    name=models.ForeignKey(House, on_delete=models.CASCADE)
    available_date=models.DateField(blank=True, null=True)
    def __str__(self):
        return self.name.name 
    
class System(models.Model):
    system_size=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cable_length=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    roof_peg_type=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    BIG='7.6kW'
    SMALL='3.8kW'
    SMARTBOX_CHOICES = ((BIG,"7.6kW"),(SMALL,"3.8kW"))
    smartbox_size = models.CharField(max_length=20, choices=SMARTBOX_CHOICES, default='3.8kW')
    smartbox_size=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    house=models.ForeignKey(House, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Receptacle_Installation(models.Model):
    name=models.CharField(max_length=200)
    cost=models.CharField(max_length=200)
    receptacle_installer=models.ForeignKey(Receptacle_Installer, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    house=models.ForeignKey(House, on_delete=models.CASCADE, null=True)
    start_date_time=models.DateTimeField(null=True)
    end_date_time=models.DateTimeField(null=True)
    def __str__(self):
        return self.name    
    
class Payment_Method(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    credit_card_no = models.DecimalField(max_digits=16, decimal_places=0, default=0)
    expiration_date = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    confirmation_code = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    system=models.ForeignKey(System, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    receptacle_installation=models.ForeignKey(Receptacle_Installation, on_delete=models.CASCADE)
    payment_method=models.ForeignKey(Payment_Method, on_delete=models.CASCADE)
    shipping_cost=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tax=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_cost=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    def __str__(self):
        return self.name
