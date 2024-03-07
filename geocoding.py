import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyCsNjtUsi1lFf398p94NKLQfFpuhDWNszE")

# Geocoding an address
geocode_result = gmaps.geocode("Avenue Charles de Gaulle 10 B, 13469, Berlin")
# print(geocode_result[0]['geometry'])

# Places
places_result = gmaps.places_nearby(location=("52.6024712", "13.3212267"), radius=1000, keyword="kita")
print(places_result)

# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions(
#     "Sydney Town Hall", "Parramatta, NSW", mode="transit", departure_time=now
# )

# # Validate an address with address validation
# addressvalidation_result = gmaps.addressvalidation(
#     ["1600 Amphitheatre Pk"],
#     regionCode="US",
#     locality="Mountain View",
#     enableUspsCass=True,
# )
