#!/usb/bin/python

traces=open("salida.txt","r")
lineas=traces.readlines()
z=0
t=0
for linea in lineas:
	if 'machine failure' in linea:
		print linea[:-1]
		x=linea.split(' ');
	
	if 'finishing repair' in linea:
		print linea[:-1]
		y=linea.split(' ');
		z=float(y[0])-float(x[0])
		print ("Tiempo parcial  fuera de  Servicio :   %4.10f."%z) 
		t=t+z

print ""  
print ("TOTAL GENERAL DE TIEMPO FUERA DE SERVICIO  :   %6.10f."%t)         

fo.close()
