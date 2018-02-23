"""3) Programa que muestra la lista de provincias 
y el total de municipios que tiene cada una."""
from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
provincias = doc.findall('provincia ')
for provincia in provincias:
	nombre = provincias.find('nombre ')
localidades = provincias.findall('localidades/localidad ')
print (nombre.text, len(localidades))
