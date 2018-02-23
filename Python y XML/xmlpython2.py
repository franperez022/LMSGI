from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
"""2) Programa que lista todos los municipios."""
municipios=doc.findall("provincia/localidades/localidad")
for i in municipios:
	print(i.text)