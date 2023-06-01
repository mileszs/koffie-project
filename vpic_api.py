import requests

def get_vehicle_by_vin(vin):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{vin}?format=json"

    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()
        return result['Results'][0]
    else:
        raise ValueError(f"Request to vPIC API failed with status code {response.status_code}")