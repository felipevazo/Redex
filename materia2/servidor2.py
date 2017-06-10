import socket
import threading

class Server():

	def __init__(self):
		self.host='localhost'
		self.port=9999
		self.maxcon=10

	def start(self):

		self.s = socket.socket()
		self.s.bind((self.host,self.port)) # doble parentesis pq se utiliza tupla, direccion en STRING 
		self.s.listen(self.maxcon)  #explicado mas adelante
		while True:
			cliente1=self.s.accept()
			cliente2=self.s.accept()# Retorna 2 valores, socket cliente y direccion cliente, socket cliente -> 
			cliente=Client(cliente1,cliente2)
			cliente.start()
            #crear nuevo socket para seguir habilitando el primero
               # Python tiene asignacion multiple CTM
                # addr= tupla similar a la del bind
class Client(threading.Thread): # En biblioteca Threading.thread, esta metodo START, crea los hilos y despues corre por si solo
								# Facilita pega haciendo cosas solito 
	
	def __init__(self,(sc,addr),(sc2,addr2)):
		threading.Thread.__init__(self)
		self.sc1=sc
		self.addr1=addr
		self.sc2=sc2
		self.addr2=addr2
	def run(self):
			
		while True:
			recibido = self.sc.recv(1024)
			if recibido == "quit":
				break    
			print recibido
			self.sc.send(recibido)
		print "shao"
		self.sc.close()
if __name__ == '__main__':
	server =Server()
	server.start()


