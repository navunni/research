import requests

api_key = "private_key" 

# please input your own API key into this to test the code out. 

def get_nearest_emergency_room(address):
    code_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(code_url)
    code_data = response.json()

    if code_data['status'] != 'OK':
        print(f"Error geocoding address: {code_data['status']}")
        return None

    location = code_data['results'][0]['geometry']['location']
    latitude = location['lat']
    longitude = location['lng']

    # Finds nearby emergency rooms

    places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=5000&type=hospital&keyword=emergency&key={API_KEY}"
    response = requests.get(places_url)
    places_data = response.json()

    if places_data['status'] != 'OK':
        print(f"Error finding places: {places_data['status']}")
        return None

    if not places_data['results']:
        print("No emergency rooms have been found nearby.")
        return None
    
    # Gets the location of the nearest emergency room. 

    nearest_place = places_data['results'][0]
    place_id = nearest_place['place_id']

    # Calculates the distance between inputted location and emergency room location.

    distance_url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={latitude},{longitude}&destinations=place_id:{place_id}&key={API_KEY}"
    response = requests.get(distance_url)
    distance_data = response.json()

    if distance_data['status'] != 'OK':
        print(f"Error calculating distance: {distance_data['status']}")
        return None

    travel_distance = distance_data['rows'][0]['elements'][0]['distance']['text']
    travel_duration = distance_data['rows'][0]['elements'][0]['duration']['text']

    return {
        'emergency_room_name': nearest_place['name'],
        'emergency_room_address': nearest_place['vicinity'],
        'travel_distance': travel_distance,
        'travel_duration': travel_duration
    }

    # how the code ideally functions (inputting your residential address, and then getting a specific calculation of the distance to the closest location)

if __name__ == "__main__":
    address = input("Please enter a residential address of your own choice: ")
    nearest_emergency_room = get_nearest_emergency_room(address)

    if nearest_emergency_room:
        print(f"Nearest Emergency Room: {nearest_emergency_room['emergency_room_name']}")
        print(f"Address: {nearest_emergency_room['emergency_room_address']}")
        print(f"Distance: {nearest_emergency_room['travel_distance']}")
        print(f"Duration: {nearest_emergency_room['travel_duration']}")

# Next Task: find the average amount of transit time between inputted location to the nearest emergency room. 