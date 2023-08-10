from django import forms

class GetCar(forms.Form):
    car_brand = forms.CharField(label="Car Brand", widget=forms.TextInput(attrs={'class': 'form-control'}))
    car_model = forms.CharField(label="Car Model", widget=forms.TextInput(attrs={'class': 'form-control'}))
    car_cc = forms.IntegerField(label="Car Displacement", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    car_transmission = forms.CharField(label="Car Transmission", widget=forms.TextInput(attrs={'class': 'form-control'}))
    car_color = forms.CharField(label="Car Color", widget=forms.TextInput(attrs={'class': 'form-control'}))
    car_hp = forms.FloatField(label="Horspower", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    car_torque = forms.FloatField(label="Torque", widget=forms.NumberInput(attrs={'class': 'form-control'}))
