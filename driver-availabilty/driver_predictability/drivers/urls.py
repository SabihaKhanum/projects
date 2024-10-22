from django.urls import path
from .views import distance_checker, calculate_distance

urlpatterns = [
    path('distance-checker/', distance_checker, name='distance_checker'),
    path('api/drivers/calculate-distance/', calculate_distance, name='calculate_distance'),
]