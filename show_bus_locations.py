import json
import urllib2
import sys

if __name__=='__main__':
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    data = json.load(request)
    busNumber = 0
    print "Bus Line : %s" % (sys.argv[2])
    print "Number of Active Buses : %s" % (len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']))
    for i in range(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])):
        stationLat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        stationLong = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print "Bus %s is at latitude %s and longitude %s" % (busNumber,stationLat, stationLong)
        busNumber += 1
