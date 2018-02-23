"""5) Programa que lea por teclado el nombre de un 
municipio y te muestra la provincia donde se encuentra."""
from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
provincias = doc.findall('provincia ')
localidad = raw_input("dame una localidad: ") 
for provincia in provincias:
	nombre = provincia.find('nombre ')
localidades = provincia.findall('localidades/localidad ')
for localidad in localidades:
	if localidad.text == localidad:
		print localidad.text, nombre.text