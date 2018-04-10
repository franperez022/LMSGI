#5) Mostrar la lista de usuarios agrupados por localidades.

from lxml import etree
arbol = etree.parse('users.xml')
usuarios = arbol.findall("user")
listacity=[]

for usuario in usuarios:
    ciudad=usuario.findtext("city")
    if ciudad not in listacity:
        listacity.append (ciudad)

for usuario in usuarios:
	for ciudad in listacity:
		if usuario.findtext("city") == ciudad:
			print (ciudad)
			print (usuario.findtext("firstname"))
			print ("------------------------------")			
