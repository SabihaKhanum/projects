import requests

# Define the API endpoint
url = 'http://127.0.0.1:8000/api/drivers/calculate-distance/'

# Define the payload with the location name
payload = {
    'location_name': 'bengaluru'
}

# Send a POST request to the API endpoint
response = requests.post(url, json=payload)

# Print the response
if response.status_code == 200:
    print(f"Distance: {response.json()['distance_km']} km")
else:
    print(f"Error: {response.status_code} - {response.text}")