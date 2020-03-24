from firebase import firebase
from datetime import datetime
import Adafruit_ADS1x15

firebase = firebase.FirebaseApplication("https://weather-268215.firebaseio.com/", None)

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

def read_sensor(adc):

	dateTimeObj = datetime.now()
	sunshine = adc.read_adc(0, gain=GAIN) #read from A0
	rain = adc.read_adc(1, gain=GAIN) #read from A1
	thunder = adc.read_adc(2, gain=GAIN) #read from A2

	#format result to lie between 0 and 1
	sunshine = sunshine / 100000
	rain = rain / 10000
	thunder = thunder / 10000

	return dateTimeObj, sunshine, rain, thunder

def create_data(dateTimeObj, sunshine, rain, thunder):

	data = {
		'time': dateTimeObj,
		'sunshine': sunshine,
		'rain': rain,
		'thunder': thunder
	}

	return data

def main():
	dateTimeObj, sunshine, rain, thunder = read_sensor(adc)
	data = create_data(dateTimeObj, sunshine, rain, thunder)
	result = firebase.post('/users/K2P6BCIj0HbUzHwuISXR2QqMNFG2', data)
	print(result)

if __name__ == "__main__":
	main()
