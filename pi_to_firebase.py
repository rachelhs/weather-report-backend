from firebase import firebase
from datetime import datetime

firebase = firebase.FirebaseApplication("https://weather-268215.firebaseio.com/", None)
dateTimeObj = datetime.now()

data = {
	'time': dateTimeObj,
	'sunshine': '0.7535',
	'rain':'0.6693',
	'thunder':'0.2491'
}

result_R = firebase.post('/users/K2P6BCIj0HbUzHwuISXR2QqMNFG2', data)
#result_E = firebase.post('/users/IcVeeY7KNaPts4y7lZhgs5st6En1', data)
