from typing import Any
from django import http
from django.http import JsonResponse
from django.views.generic import TemplateView, FormView

from .forms import GetCar
from .models import Car

# Create your views here.
class MainHomePage(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context
    
class AddMyCar(FormView):
    template_name = "add_cars.html"
    form_class = GetCar

    def form_valid(self, form):
        new_car = Car.objects.create(
            car_brand=form.cleaned_data['car_brand'],
            car_model=form.cleaned_data['car_model'],
            car_cc=form.cleaned_data['car_cc'],
            car_transmission=form.cleaned_data['car_transmission'],
            car_color=form.cleaned_data['car_color'],
            car_hp=form.cleaned_data['car_hp'],
            car_torque=form.cleaned_data['car_torque'],
        )

        return JsonResponse({'success': True})