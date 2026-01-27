import phonenumbers
import opencage
from myphone import number

from phonenumbers import geocoder

ch_nmber = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))

 from phonenumbers import carrier

service_number = phonenumbers.parse(number,"RO")

print(carrier.name_for_number(service_number,"en"))
# number = phonenumbers.parse(number)
# location = geocoder.description_for_number(pepnumber,"en")
# print(location)


# from phonenumbers import carrier
# service_pro = phonenumbers.parse(number)
# print(carrier.name_for_number(service_pro,"en"))


# from opencage.geocoder import opencagegeocode

# key = 'f88cf10e5cb846648cedc17b30ae0eca'
# geocoder = opencagegeocode(key)
# query = str(location)
# results = geocoder.geocode(query)
# print(results)