from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Please enter API and Bus #")
    sys.exit()
    
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]
response = urllib.urlopen(url)
data = response.read().decode("utf-8")

data = json.loads(data)

Bus_Num = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print("Bus line: " + sys.argv[2])
print("Number of Active Buses: {}".format(Bus_Num))

for i in range(Bus_Num):
    Bus_lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    Bus_long = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print('Bus {} is at latitude {} and longitude {}'.format(i, Bus_lat, Bus_long))
     