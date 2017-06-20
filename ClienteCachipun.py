import socket
s=socket.socket()
s.connect(('127.0.0.1',9999))
while True:
	mensaje=s.recv(1024)
	if(mensaje=="ronda"):
		valid=True
		while(valid):
			tirada=raw_input('piedra, papel o tijeras>>')
			if(tirada!="tijeras" and tirada!="piedra" and tirada!="papel"):
				print "Entrada invalida, intente nuevamente"
			else:
				print tirada
				s.send(tirada)
				valid=False	
		valid=True
	elif(mensaje=="closing"):
		print "adios"
		break
	else:
		print mensaje
s.close()    
