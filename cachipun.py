import socket
import threading
import time




class Cachipun():
	def __init__(self,sc1,sc2, numeroPartidas):
		self.j1=sc1
		self.j2=sc2
		self.numeroPartidas=numeroPartidas
		self.ganadasj1=0
		self.ganadasj2=0
		self.crearTabla(numeroPartidas)

	def crearTabla(self, numeroPartidas):
		self.listaTablero1=["J1","-"]
		self.listaTablero2=["J2 ","-"]
		for x in range (2, numeroPartidas):
			self.listaTablero1.append("-")
			self.listaTablero2.append("-")
	def imprimeTijeras(self,sc):
		sc.send("    _       ,/'\n   (_).  ,/'\n   __  ::\n  (__)'  `\.\n            `\.")
	def imprimePapel(self,sc):
		sc.send("               _.-._\n             /| | | |_\n             || | | | |\\n           _ || | | | |\n          \\`||     ` |\n           \\ \       ;\n            \\        |\n             \\      /\n             / \     \ \n            /   \     \ ")
	def imprimePiedra(self,sc):
		sc.send  (".----.-----.-----.-----.\n /      \     \     \     \ \n|  \/    |     |   __L_____L__\n|   |    |     |  (           \ \n|    \___/    /    \______/    |\n|        \___/\___/\___/       |\n \      \     /               /\n  |                        __/\n   \_                   __/\n    |        |         |")
	def jugarDos(self, tiroJug1, tiroJug2,r):
		tiroJug1=tiroJug1.lower()
		tiroJug2=tiroJug2.lower()
		if tiroJug1 == "piedra":
			if tiroJug2=="papel":
				self.j1.send("J1\n   ")
				time.sleep(0.01)
				self.imprimePiedra(self.j1)
				time.sleep(0.01)
				self.j2.send("J1\n   ")
				time.sleep(0.01)
				self.imprimePiedra(self.j2)
				time.sleep(0.01)
				self.j1.send("J2\n   ")
				time.sleep(0.01)
				self.imprimePapel(self.j1)
				time.sleep(0.01)
				self.j2.send("J2\n   ")
				time.sleep(0.01)
				self.imprimePapel(self.j2)
				time.sleep(0.01)
				self.j1.send("Ronda para jugador 2")
				self.j2.send("Ronda para jugador 2")
				time.sleep(0.01)
				self.ganadasj2+=1
				self.listaTablero1[r]="Perdida"
				self.listaTablero2[r]="Ganada"
			elif tiroJug2=="tijeras":
				self.listaTablero2[r]="Perdida"
				self.listaTablero1[r]="Ganada"
				self.j1.send("J1\n   ")
				time.sleep(0.01)
				self.imprimePiedra(self.j1)
				time.sleep(0.01)
				self.j2.send("J1\n   ")
				time.sleep(0.01)
				self.imprimePiedra(self.j2)
				time.sleep(0.01)
				self.j1.send("J2\n   ")
				time.sleep(0.01)
				self.imprimeTijeras(self.j1)
				time.sleep(0.01)
				self.j2.send("J2\n   ")
				time.sleep(0.01)
				self.imprimeTijeras(self.j2)
				time.sleep(0.01)
				self.j1.send("Ronda para jugador 1\n")
				self.j2.send("Ronda para jugador 1\n")
				time.sleep(0.01)
				self.ganadasj1+=1
				# aqui se anadira a tabla
			elif tiroJug2=="piedra":
				self.j1.send("J1   ")
				time.sleep(0.01)
				self.imprimePiedra(self.j1)
				time.sleep(0.01)
				self.j2.send("J1\n   ")
				time.sleep(0.01)
				self.imprimePiedra(self.j2)
				time.sleep(0.01)
				self.j1.send("J2\n   ")
				time.sleep(0.01)
				self.imprimePiedra(self.j1)
				time.sleep(0.01)
				self.j2.send("J2\n   ")
				time.sleep(0.01)
				self.imprimePiedra(self.j2)
				time.sleep(0.01)
				self.j1.send("empate, se repite la ronda\n")
				self.j2.send("empate, se repite la ronda\n")
			else:
				self.j2.send("Ingrese palabras correctas J2, piedra, papel o tijeras\n")
		elif tiroJug1=="tijeras":
			if tiroJug2=="papel":
				self.j1.send("J1\n   ")
				time.sleep(0.01)
				self.imprimeTijeras(self.j1)
				time.sleep(0.01)
				self.j2.send("J1\n   ")
				time.sleep(0.01)
				self.imprimeTijeras(self.j2)
				time.sleep(0.01)
				self.j1.send("J2\n   ")
				time.sleep(0.01)
				self.imprimePapel(self.j1)
				time.sleep(0.01)
				self.j2.send("J2\n   ")
				time.sleep(0.01)
				self.imprimePapel(self.j2)
				time.sleep(0.01)
				self.j1.send("Ronda para jugador 1\n")
				self.j2.send("Ronda para jugador 1\n")
				time.sleep(0.01)
				self.listaTablero2[r]="Perdida\n"
				self.listaTablero1[r]="Ganada\n"
				self.ganadasj1+=1
				# aqui se anadira a tabla
			elif tiroJug2=="piedra":
				self.j1.send("J1\n   ")
				time.sleep(0.01)
				self.imprimeTijeras(self.j1)
				time.sleep(0.01)
				self.j2.send("J1\n   ")
				time.sleep(0.01)
				self.imprimeTijeras(self.j2)
				time.sleep(0.01)
				self.j1.send("J2\n   ")
				time.sleep(0.01)
				self.imprimePiedra(self.j1)
				time.sleep(0.01)
				self.j2.send("J2\n   ")
				time.sleep(0.01)
				self.imprimePiedra(self.j2)
				time.sleep(0.01)
				self.j1.send("Ronda para jugador 2\n")
				self.j2.send("Ronda para jugador 2\n")
				time.sleep(0.01)
				self.listaTablero1[r]="Perdida\n"
				self.listaTablero2[r]="Ganada\n"
				self.ganadasj2+=1
				# aqui se anadira a tabla
			elif tiroJug2=="tijeras":
				self.j1.send("J1\n   ")
				time.sleep(0.01)
				self.imprimeTijeras(self.j1)
				time.sleep(0.01)
				self.j2.send("J1\n   ")
				time.sleep(0.01)
				self.imprimeTijeras(self.j2)
				time.sleep(0.01)
				self.j1.send("J2\n   ")
				time.sleep(0.01)
				self.imprimeTijeras(self.j1)
				time.sleep(0.01)
				self.j2.send("J2\n   ")
				time.sleep(0.01)
				self.imprimeTijeras(self.j2)
				time.sleep(0.01)
				self.j2.send( "Empate, se repite la ronda\n")
				self.j1.send( "Empate, se repite la ronda\n")
			else:
				self.j2.send("Ingrese palabras correctas J2, piedra, papel o tijeras\n")
		elif tiroJug1=="papel":
			if tiroJug2 == "tijeras":
				self.j1.send("J1\n   ")
				time.sleep(0.01)
				self.imprimePapel(self.j1)
				time.sleep(0.01)
				self.j2.send("J1\n   ")
				time.sleep(0.01)
				self.imprimePapel(self.j2)
				time.sleep(0.01)
				self.j1.send("J2\n   ")
				time.sleep(0.01)
				self.imprimeTijeras(self.j1)
				time.sleep(0.01)
				self.j2.send("J2\n   ")
				time.sleep(0.01)
				self.imprimeTijeras(self.j2)
				time.sleep(0.01)
				self.j1.send("Ronda para jugador 2\n")
				self.j2.send("Ronda para jugador 2\n")
				self.listaTablero1[r]="Perdida\n"
				self.listaTablero2[r]="Ganada\n"
				time.sleep(0.01)
				self.ganadasj2+=1
				# aqui se anadira a tabla
			elif tiroJug2=="papel":
				self.j1.send("J1\n   ")
				time.sleep(0.01)
				self.imprimePapel(self.j1)
				time.sleep(0.01)
				self.j2.send("J1\n   ")
				time.sleep(0.01)
				self.imprimePapel(self.j2)
				time.sleep(0.01)
				self.j1.send("J2\n   ")
				time.sleep(0.01)
				self.imprimePapel(self.j1)
				time.sleep(0.01)
				self.j2.send("J2\n   ")
				time.sleep(0.01)
				self.imprimePapel(self.j2)
				time.sleep(0.01)
				self.j2.send( "Empate, se repite la ronda\n")
				self.j1.send( "Empate, se repite la ronda\n")
				time.sleep(0.01)
				# aqui se anadira a tabla
			elif tiroJug2=="piedra":
				self.j1.send("J1\n   ")
				time.sleep(0.01)
				self.imprimePapel(self.j1)
				time.sleep(0.01)
				self.j2.send("J1\n   ")
				time.sleep(0.01)
				self.imprimePapel(self.j2)
				time.sleep(0.01)
				self.j1.send("J2\n   ")
				time.sleep(0.01)
				self.imprimePiedra(self.j1)
				time.sleep(0.01)
				self.j2.send("J2\n   ")
				time.sleep(0.01)
				self.imprimePiedra(self.j2)
				time.sleep(0.01)
				self.j1.send("Ronda para jugador 1\n")
				self.j2.send("Ronda para jugador 1\n")
				time.sleep(0.01)
				self.listaTablero2[r]="Perdida\n"
				self.listaTablero1[r]="Ganada\n"
				self.ganadasj2+=1
			else:
				
				self.j2.send("Ingrese palabras correctas J2, piedra, papel o tijeras\n")
		else:
			self.j1.send("Ingrese palabras correctas J1, piedra, papel o tijeras\n")

	def torneo(self):
		for x in range(0, self.numeroPartidas):
			if(self.ganadasj2>(self.numeroPartidas/2)):
				self.j1.send( "Jugador 2 GANA ")	
				self.j2.send( "Jugador 2 GANA ")
				time.sleep(0.1)
				break
			elif(self.ganadasj1>(self.numeroPartidas/2)):
				self.j1.send( "Jugador 1 GANA \n")
				self.j2.send( "Jugador 1 GANA \n")
				time.sleep(0.1)
				break
			time.sleep(1)
			self.j1.send("ronda")
			time.sleep(1)
			self.j2.send("ronda")
			tiroJug1=self.j1.recv(1024)
			tiroJug2=self.j2.recv(1024)
			print tiroJug1
			print tiroJug2
			self.jugarDos(tiroJug1, tiroJug2, x)
			if(x<(self.ganadasj1+self.ganadasj2)):
				x=x-1
			self.mostrarTabla()
		
	def mostrarTabla(self):
		for x in range (0, self.numeroPartidas):
			self.j1.send( self.listaTablero1[x] +"   " +self.listaTablero2[x]+"\n   ")
			self.j2.send( self.listaTablero1[x] +"   " +self.listaTablero2[x]+"\n   ")
			time.sleep(0.006)
				

class Server():

	def __init__(self):
		self.host='localhost'
		self.port=9999
		self.maxcon=10

	def start(self):

		self.s = socket.socket()
		self.s.bind((self.host,self.port)) 
		self.s.listen(self.maxcon)  #explicado mas adelante
		while True:
			(sc1,addr1)=self.s.accept()
			sc1.send("Espere")
			(sc2,addr2)=self.s.accept()
			sc1.send("Ok J1")
			sc2.send("Ok J2")# Retorna 2 valores, socket cliente y direccion cliente, socket cliente -> 
			cliente=Client((sc1,addr1),(sc2,addr2))
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
			
		self.cachipun=Cachipun(self.sc1,self.sc2,5)
		self.cachipun.torneo()
		sc1.send("closing")
		sc2.send("closing")
if __name__ == '__main__':
	server =Server()
	server.start()




