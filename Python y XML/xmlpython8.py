"""8) Programa que lea una localidad y te diga si es "ciudad 
grande" (atributo c="1") o no de provincia. Si es "ciudad grande" 
de provincia te muestra su nombre."""
from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
poblacion= input("Dime un municipio: ")
provincias= doc.findall("provincia")
for provincia in provincias:
	localidades=provincia[1].findall("localidad")
	for localidad in localidades:
		if localidad.text == poblacion:
			if localidad.attrib["c"]=="1":
				print (poblacion, "es ciudad grande de", provincia[0].text)
			else:
				print (poblacion, "no es ciudad grande" )

