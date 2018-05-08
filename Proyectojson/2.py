#2. Contar cuantos coches son de "USA" de origen.

import json

from pprint import pprint

with open("coches.json") as data_file:
	data=json.load(data_file)
contador=0

for origen in data:
	if origen["Origin"] == "USA":
		contador=contador+1
print("Hay ",contador," coches matriculados en USA")


