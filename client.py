from geopy.geocoders import Nominatim
import csv

print("========================================================================")
print("This tool is for reporting infrastructure damage to emergency responce crews.\nIf you or someone you know is experiencing an emergency, call emergency services.")
print("========================================================================")

#get user address using geopy
while True:
    try:
        print("Input your address:\n")
        address = input()

        geolocator = Nominatim(user_agent="UTEK25")
        location = geolocator.geocode(address)

        print("Is your address " + location.address + " (Y/N)\n")
        roadCorrect = input()
        if roadCorrect == 'Y' or roadCorrect == 'y' or roadCorrect == 'yes':
            break
        else:
            continue
    except AttributeError:
        print("Invalid address. Try again\n")


latlng = [location.latitude,location.longitude]

#get report type
print("Is there road blockage / damage at your location? (Y/N)\n")

road = input()
if road == 'Y' or road == 'Yes' or road == 'y':
    road = 1
else:
    road = 0

print("Is there a collapsed building at your location? (Y/N)\n")

building = input()
if building == 'Y' or building == 'Yes' or building == 'y':
    building = 1
else:
    building = 0

print("Is water running at your location? (Y/N)\n")

water = input()
if water == 'Y' or water == 'Yes' or water == 'y':
    water = 1
else:
    water = 0

print("Is electricity running at your location? (Y/N)\n")

electricity = input()
if electricity == 'Y' or electricity == 'Yes' or electricity == 'y':
    electricity = 1
else:
    electricity = 0

print("Is gas working at your location? (Y/N)\n")

gas = input()
if gas == 'Y' or gas == 'Yes' or gas == 'y':
    gas = 1
else:
    gas = 0


#write data to database
data = [latlng[0],latlng[1],road,building,water,electricity,gas]

with open('reports.csv', 'a', newline='') as file:
    writer = csv.writer(file)   
    writer.writerow(data)

