#2) Mostrar el nombre de usuario de los usarios que han 
#cambiado su avatar en nuestra plataforma moodle (Elemento 
#picture)

from lxml import etree
arbol = etree.parse('users.xml')
usuarios = arbol.findall("user")
for usuario in usuarios:
	#Que empiece por 1
	if usuario.findtext("picture").startswith("1"): 
		#print el campo texto username
		print (usuario.find("username").text)