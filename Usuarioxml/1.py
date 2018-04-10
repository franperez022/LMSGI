#1) Lista de usuarios (profesores y alumnos) matriculados 
#en el módulo "Lenguaje de marcas". )

from lxml import etree
arbol = etree.parse('users.xml')
usuarios = arbol.findall("user")
for usuario in usuarios:
	print (usuario.find("firstname").text)
	print (usuario.find("lastname").text)