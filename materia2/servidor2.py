import socket

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
			client=Client(self.s.accept())# Retorna 2 valores, socket cliente y direccion cliente, socket cliente -> 
			client.run() 
            #crear nuevo socket para seguir habilitando el primero
               # Python tiene asignacion multiple CTM
                # addr= tupla similar a la del bind
class Client():
	
	def __init__(self,(sc,addr)):
		self.sc=sc
		self.addr=addr
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

