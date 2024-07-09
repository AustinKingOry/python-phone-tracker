import phonenumbers
from myphone import number

import opencage
from opencage.geocoder import OpenCageGeocode

from phonenumbers import geocoder,carrier

import folium

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
service_pro = carrier.name_for_number(phonenumbers.parse(number),"en")
print(location+" "+service_pro)

key = "4006518471eb4421880c8e60cddb5539"
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
# print(result)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map([lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("myloc.html")