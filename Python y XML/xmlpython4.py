"""4) Programa que lea por teclado el nombre de una 
provincia y muestra sus municipios."""
from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
provincias = doc.findall('provincia ')
prov = input("dame una provincia: ")
for provincia in provincias:
	nombre = provincia.find('nombre ')
	if nombre.text == prov:
		localidades = provincia.findall('localidades/localidad ')
for localidad in localidades:
    print (localidad.text)
	
