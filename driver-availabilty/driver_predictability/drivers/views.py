from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from geopy.distance import geodesic
import requests
import os
from dotenv import load_dotenv

def distance_checker(request):
    print("Distance checker view called")  # Debugging line
    return render(request, 'drivers/distance_checker.html')



# Replace 'YOUR_OPENCAGE_API_KEY' with your actual OpenCage API key
load_dotenv()
API_KEY = os.getenv('API_KEY')
OPENCAGE_URL = 'https://api.opencagedata.com/geocode/v1/json'

# @csrf_exempt 
@api_view(['POST'])
def calculate_distance(request):
    print("api view called")
    if request.method == 'POST':
        data = json.loads(request.body)
        location_name = data.get('location_name')
        current_location = {"lat": 34.0522, "lng": -118.2437}  # Los Angeles coordinates

        # Get the user-entered location name from the request
        location_name = request.data.get('location_name')  # Expecting a string

        if not location_name:
            return JsonResponse({'error': 'location_name is required.'}, status=400)

        # Geocode the location name to get latitude and longitude
        geocode_response = requests.get(OPENCAGE_URL, params={
            'q': location_name,
            'key': OPENCAGE_API_KEY
        })

        if geocode_response.status_code != 200:
            return JsonResponse({'error': 'Failed to geocode location.'}, status=geocode_response.status_code)

        geocode_data = geocode_response.json()

        if not geocode_data['results']:
            return JsonResponse({'error': 'Location not found.'}, status=404)

        # Extract latitude and longitude from the geocoding response
        entered_coords = (
            geocode_data['results'][0]['geometry']['lat'],
            geocode_data['results'][0]['geometry']['lng']
        )

        # Calculate the distance
        distance = geodesic((current_location['lat'], current_location['lng']), entered_coords).kilometers

        return JsonResponse({'distance_km': distance})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
