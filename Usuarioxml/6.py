#6) Mostrar la lista de ususarios ordenada por el último acceso 
#(Elemento lastaccess)
from lxml import etree
arbol = etree.parse('users.xml')
usuarios = arbol.findall("user")
listaacceso=[]

for usuario in usuarios:
    acceso=usuario.findtext("lastaccess")
    listaacceso.append (acceso)
    listaacceso.sort() # ordena la lista
    listaacceso.reverse() # le da la vuelta a la lista
 # para imprimir la lista en formato largo
for x in listaacceso:
	print(x)