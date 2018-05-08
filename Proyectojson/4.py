#4. Pedir por teclado una aceleración (con 1 decimal) y te muestre todos los coches
#que tienen menor aceleración que la indicada.
import json

from pprint import pprint

with open("coches.json") as data_file:
	data=json.load(data_file)
aceleracionindicada=float(input("Dame una aceleración: (1 decimal) "))
for aceleracion in data:
	if aceleracion["Acceleration"] < aceleracionindicada:
		print(aceleracion["Name"])
	if aceleracionindicada != aceleracion["Acceleration"]:
		print ("No hay ninguno.")

