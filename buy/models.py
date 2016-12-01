from __future__ import unicode_literals

from django.db import models

from django.utils import timezone


class Customer(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Receptacle_Installer(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Roof_Mount_Installer(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Appliance_Installer(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Appliance_Installer(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Receptacle_Installation(models.Model):
    name=models.CharField(max_length=200)
    cost=models.CharField(max_length=200)
    receptacle_installer=models.ForeignKey(Receptacle_Installer, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Roof_Mount_Installation(models.Model):
    date=models.CharField(max_length=200)
    cost=models.CharField(max_length=200)
    roof_mount_installer=models.ForeignKey(Roof_Mount_Installer, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Appliance_Installation(models.Model):
    date=models.CharField(max_length=200)
    cost=models.CharField(max_length=200)
    appliance_installer=models.ForeignKey(Appliance_Installer, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class House(models.Model):
    address=models.CharField(max_length=200)
    insolation=models.IntegerField(default=5)
    roof_slope=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    roof_area=models.DecimalField(max_digits=9, decimal_places=2, default=3000)
    monthly_electricity_usage=models.DecimalField(max_digits=5, decimal_places=0, default=600)
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
    ONESTORY='One Story'
    TWOSTORIES='Two Stories'
    THREESTORIES='Three Stories'
    HEIGHT_CHOICES = ((ONESTORY,"One Story"),(TWOSTORIES,"Two Stories"),(THREESTORIES,"Three Stories"))
    stories=models.CharField(max_length=200, choices=HEIGHT_CHOICES, default='One Story')
    roof_height=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    busbar_capacity=models.DecimalField(max_digits=9, decimal_places=0, default=100)
    main_breaker_size=models.DecimalField(max_digits=9, decimal_places=0, default=100)
    YES='Yes'
    NO='No'
    IDK='Help me figure it out'
    ROOM_CHOICES = ((YES,"Yes"),(NO,"No"),(IDK,"Help me figure it out"))
    is_there_room_for_new_breaker_opposite_main_breaker=models.CharField(max_length=200, choices=ROOM_CHOICES, default="Yes")
    def __str__(self):
        return self.address

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
    roof_mount_installation=models.ForeignKey(Roof_Mount_Installation, on_delete=models.CASCADE)
    appliance_installation=models.ForeignKey(Appliance_Installation, on_delete=models.CASCADE)
    payment_method=models.ForeignKey(Payment_Method, on_delete=models.CASCADE)
    shipping_cost=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tax=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_cost=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    def __str__(self):
        return self.name
