#!/usb/bin/python

fo=open("salida.txt","r")
lineas=fo.readlines()
z=0
t=0
for linea in lineas:
	if 'starting repair' in linea:
		print linea[:-1]
		x=linea.split(' ');
	
	if 'finishing repair' in linea:
		print linea[:-1]
		y=linea.split(' ');
		z=float(y[0])-float(x[0])
		print ("Tiempo parcial  tardado en reparacion :   %4.10f."%z) 
		t=t+z

print ""  
print ("TOTAL GENERAL TIEMPO  DE REPARACION  :   %6.10f."%t) 
fo.close()
