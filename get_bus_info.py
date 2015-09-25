import json
import urllib2
import sys
import csv


if __name__=='__main__':
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    data = json.load(request)
    vehicleActivity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude','Stop Name','Stop Status']
        writer.writerow(headers)
        for i in range(len(vehicleActivity)):
            Latitude = vehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            Longitude  = vehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            if vehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls']:
                stopName = vehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                stopStatus = vehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            else:
                stopName = "N/A"
                stopStatus = "N/A"
            writer.writerow([Latitude,Longitude,stopName,stopStatus])