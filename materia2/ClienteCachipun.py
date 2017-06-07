import socket()
s=socket.socket()
s.connect(('127.0.0.1',9999))
while True:
	mensaje=s.rcv(1024)
	if(mensaje=="Ronda"):
		valid=True
		while(valid):
			tirada=raw_input('piedra, papel o tijeras>>')
			if(tirada!="tijeras"&&tirada!="piedra"&&tirada!="papel"):
				print "Entrada invalida, intente nuevamente"
			else:
				valid=False	
	elif(mensaje=="closing"):
		print "adios"
		break
	else:
		print mensaje
s.close()    
