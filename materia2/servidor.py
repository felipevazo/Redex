import socket

s = socket.socket()
s.bind(('127.0.0.1',9999)) # doble parentesis pq se utiliza tupla, direccion en STRING 
s.listen(1) # explicado mas adelante
sc, addr = s.accept() # Retorna 2 valores, socket cliente y direccion cliente, socket cliente -> 
            #crear nuevo socket para seguir habilitando el primero
               # Python tiene asignacion multiple CTM
                # addr= tupla similar a la del bind
while True:
    recibido = sc.recv(1024) # recv= recibido
    if recibido == "quit":
        break    
    print recibido
    sc.send(recibido)
sc.close()
s.close()
