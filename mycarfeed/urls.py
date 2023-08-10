from django.urls import path
from .views import MainHomePage, AddMyCar

app_name = 'mycarfeed'

urlpatterns = [
    path('', MainHomePage.as_view(), name='index'),
    path('addcars/', AddMyCar.as_view(), name='add_car'),
]