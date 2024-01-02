from django.urls import path
from . import views

urlpatterns = [
    path('addStixData/', views.add_stix_data, name='add_stix_data'),
]
