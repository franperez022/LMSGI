""" En una lista tenemos distintos identificadores de provincias, mostrar el 
nombre de las provincias y todos los municipios correspondientes a los 
identificadores que se encuentran en la lista."""
lista=["01", "02", "03", "05", "07"]
from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
provincias = doc.findall('provincia')
for provincia in provincias: 
	if provincia.attrib ["id"]in lista:
		print("provincia: ", provincia[0].text)
		localidades = provincia[1].findall ("localidad")
		for localidad  in localidades:
			print(localidad.text)

