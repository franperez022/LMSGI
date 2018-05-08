#3. Buscar y listar los coches que superen los 100cv.
import json

from pprint import pprint

with open("coches.json") as data_file:
	data=json.load(data_file)

for cv in data:
	
	if int(cv["Horsepower"]) >= 100:
		print(cv["Name"])


