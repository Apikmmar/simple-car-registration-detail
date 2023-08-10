from django.db import models

# Create your models here.
# once created make migration - python manage.py makemigrations, then python manage.py migrate then register in admin
class Car(models.Model):
    car_brand = models.CharField(max_length=200, blank=False, null=False)
    car_model = models.CharField(max_length=200, blank=False, null=False)
    car_cc = models.IntegerField(blank=False, null=False)
    car_transmission = models.CharField(max_length=200, blank=False, null=False)
    car_color = models.CharField(max_length=200, blank=False, null=False)
    car_hp = models.FloatField(max_length=200, blank=False, null=False)
    car_torque = models.FloatField(max_length=200, blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.car_brand} {self.car_model}"