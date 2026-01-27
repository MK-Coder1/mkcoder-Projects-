import phonenumbers # type: ignore
import opencage # type: ignore
import folium # type: ignore
from myphone import number

from phonenumbers import geocoder # type: ignore

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier # type: ignore
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode # type: ignore


# key = '0ebdf19437ce4eaf8aba8abf6eee7745'
key = '99d33e12298f484cb8830b21bea3c9db'
 
geocoder = OpenCageGeocode(key)
 
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")