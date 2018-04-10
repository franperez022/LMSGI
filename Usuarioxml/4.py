#4) Pedir una cadena por teclado y mostrar todos los usarios 
#cuyo nombre empieza por dicha cadena (Ejemplo: si meto la cadena "A" 
#mostrará todos los usuarios cuyo nombre empeiza por A...)

from lxml import etree
arbol = etree.parse('users.xml')
usuarios = arbol.findall("user")
cadena = input("Introduce una letra: ")
for usuario in usuarios:
	#Que empiece por la cadena introducida 
	if usuario.findtext("firstname").startswith(cadena): 
		#print el campo texto user name cuyo 
		#nombre empieza por cadena
		print (usuario.find("username").text)