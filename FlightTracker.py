import RPi.GPIO as GPIO
from FlightRadar24 import FlightRadar24API
fr_api = FlightRadar24API()
GPIO.setmode(GPIO.BOARD)
GPIO.setup([11,12,13], GPIO.OUT)
GPIO.setwarnings(False)
import time

flight_number = ""

#Your point is 52°34'04.7"N 13°16'57.5"E from Google Maps and radius 4km
bounds = fr_api.get_bounds_by_point(38.85142578959205, -77.0401564025055, 70000)

flights = fr_api.get_flights( bounds = bounds) #gets all of the flights within a

def is_landing(dist):
    if dist <=50 and dist > 10:
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(13, GPIO.HIGH)
        
    if dist <= 1:
        GPIO.output(12, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(12, GPIO.LOW)
        time.sleep(0.5)
            
            
def is_flight_live(flight_info):
    if 'status' in flight_info:
        status = flight_info['status']['live']
        if status == True:
            return True
    return False

#loop that iterates through all flight objects
for flight in flights:
    if flight.number == flight_number:
        #getting the flight details and airport
        flight_details = fr_api.get_flight_details(flight)
        #getting the distance that flight is from airport
        live = is_flight_live(flight_details)
        #arriving = is_flight_arriving(flight_details)
        airport = fr_api.get_airport("DCA")
        distance = flight.get_distance_from(airport)
        if live==True:
            is_landing(distance)
GPIO.cleanup()
