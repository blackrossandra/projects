from datetime import datetime
import geocoder
from geopy.geocoders import Nominatim
from os import system, name

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

clear()

print('\n')
print('''
██████╗░██████╗░░█████╗░██╗░░██╗███████╗███╗░░██╗  ░██████╗░█████╗░██████╗░██╗██████╗░████████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝
██████╦╝██████╔╝██║░░██║█████═╝░█████╗░░██╔██╗██║  ╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░
██╔══██╗██╔══██╗██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░
██████╦╝██║░░██║╚█████╔╝██║░╚██╗███████╗██║░╚███║  ██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░''')
print('\n','\n')
answer=input('¿Empezar el juego? (si/no): ')

if answer.lower()=='si':

	clear()

	print('''
ELIJE UNA OPCIÓN:
  (1) QUIERO SABER QUÉ HORA ES
  (2) QUIERO SABER QUÉ DÍA ES
  (3) QUIERO SABER DÓNDE ESTOY (No Fiable)

	''')
	answer=input('SELECCIONA UNA OPCIÓN (1-3): ') 

	if answer.lower()=='1':
		now = datetime.now()

		clear()

		current_time = now.strftime("%H:%M:%S")
		print("\nHora actual =", current_time)
		answer=input('')
	 
	if answer.lower()=='2':
		now = datetime.now()

		clear()

		print("\nHoy es día %s/%s/%s" % (now.day, now.month, now.year))
		answer=input('')

	if answer.lower()=='3':
		g = geocoder.ip('me')

		clear()

		print(g.latlng)

		geolocator = Nominatim(user_agent="coordinateconverter")
		address = (g.latlng)
		location = geolocator.reverse(address)
		print(location)
		print('\nGracias por jugar.')

		answer=input('')

clear()