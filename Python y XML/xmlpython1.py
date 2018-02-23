from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
"""1) Programa que lista todas las provincias."""
raiz=doc.getroot()
provincias=raiz[0]
for x in range (len(raiz)):
	provincias=raiz[x]
	print (provincias[0].text)

