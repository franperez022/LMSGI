#1. Listar todos los coches, mostrar nombre y modelo.

import json

from pprint import pprint

with open("coches.json") as data_file:
	data=json.load(data_file)

for nombre in data:

	print(nombre["Name"])