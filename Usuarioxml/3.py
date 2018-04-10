#Mostrar los correos electrónicos de los usuarios 
#que han accedido por última vez desde fuera del instituto 
#(elemento lastip)

from lxml import etree
arbol = etree.parse('users.xml')
usuarios = arbol.findall("user")
for usuario in usuarios:
	#Que empiece por la ip 
	if usuario.findtext("lastip").startswith("172.22"): 
		#print el campo texto email
		print (usuario.find("email").text)