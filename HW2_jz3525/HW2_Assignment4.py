from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Please enter API, Bus # and CSV path")
    sys.exit()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

Bus_Num = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

with open(sys.argv[3], 'w') as f:
    f.writelines("Latitude,Longitude,Stop Name,Stop Status\n")
    for i in range(Bus_Num):
        Bus_lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        Bus_long = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        if data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls'] == {}:
            StopPointName = "N/A"
            PresentableDistance = "N/A"
        else:
            StopPointName = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
            PresentableDistance = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        f.writelines(str(Bus_lat) + ', ' + str(Bus_long) + ', ' + str(StopPointName) + ', ' + str(PresentableDistance) + '\n')
            