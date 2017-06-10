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
			cliente1.send("Espere")
			cliente2=self.s.accept()
			cliente2.send("Ok J1")
			cliente1.send("Ok J2")# Retorna 2 valores, socket cliente y direccion cliente, socket cliente -> 
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
			
		cachipun=Cachipun(sc1,sc2,5)
		cachipun.torneo()
		sc1.send("closing")
		sc2.send("closing")
if __name__ == '__main__':
	server =Server()
	server.start()





class Cachipun():
	def __init__(self,sc1,sc2, numeroPartidas):
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
		sc.send("    _       ,/'")
		sc.send("   (_).  ,/'")
		sc.send("   __  ::")
		sc.send("  (__)'  `\.")
		sc.send("            `\.")
	def imprimePapel(self,sc):
		sc.send("               _.-._")
		sc.send("             /| | | |_")
		sc.send("             || | | | |")
		sc.send("           _ || | | | |")
		sc.send("          \\`||     ` |")
		sc.send("           \\ \       ;")
		sc.send("            \\        |")
		sc.send("             \\      /")
		sc.send("             / \     \")
		sc.send("            /   \     \")
	def imprimePiedra(self,sc):
			sc.send("  .----.-----.-----.-----.")
			sc.send(" /      \     \     \     \")
			sc.send("|  \/    |     |   __L_____L__")
			sc.send("|   |    |     |  (           \")
			sc.send("|    \___/    /    \______/    |")
			sc.send("|        \___/\___/\___/       |")
			sc.send(" \      \     /               /")
			sc.send("  |                        __/")
			sc.send("   \_                   __/")
			sc.send("    |        |         |")
			sc.send("    |                  |")
			sc.send("    |                  |")
			
		
		
		
	def jugarDos(self, tiroJug1, tiroJug2,r):
		tiroJug1=tiroJug1.lower()
		tiroJug2=tiroJug2.lower()
		if tiroJug1 == "piedra":
			if tiroJug2=="papel":
				self.sc1.send("J1")
				self.sc1.send("   ")
				self.imprimePiedra(self.sc1)
				self.sc2.send("J1")
				self.sc2.send("   ")
				self.imprimePiedra(self.sc2)
				self.sc1.send("J2")
				self.sc1.send("   ")
				self.imprimePapel(self.sc1)
				self.sc2.send("J2")
				self.sc2.send("   ")
				self.imprimePapel(self.sc2)
				self.sc1.send("Ronda para jugador 2")
				self.sc2.send("Ronda para jugador 2")
				self.ganadasj2+=1
				self.listaTablero1[r]="Perdida"
				self.listaTablero2[r]="Ganada"
			elif tiroJug2=="tijeras":
				self.listaTablero2[r]="Perdida"
				self.listaTablero1[r]="Ganada"
				self.sc1.send("J1")
				self.sc1.send("   ")
				self.imprimePiedra(self.sc1)
				self.sc2.send("J1")
				self.sc2.send("   ")
				self.imprimePiedra(self.sc2)
				self.sc1.send("J2")
				self.sc1.send("   ")
				self.imprimeTijeras(self.sc1)
				self.sc2.send("J2")
				self.sc2.send("   ")
				self.imprimeTijeras(self.sc2)
				self.sc1.send("Ronda para jugador 1")
				self.sc2.send("Ronda para jugador 1")
				self.ganadasj1+=1
				# aqui se anadira a tabla
			elif tiroJug2=="piedra":
				self.sc1.send("J1")
				self.sc1.send("   ")
				self.imprimePiedra(self.sc1)
				self.sc2.send("J1")
				self.sc2.send("   ")
				self.imprimePiedra(self.sc2)
				self.sc1.send("J2")
				self.sc1.send("   ")
				self.imprimePiedra(self.sc1)
				self.sc2.send("J2")
				self.sc2.send("   ")
				self.imprimePiedra(self.sc2)
				self.sc1.send("empate, se repite la ronda")
				self.sc2.send("empate, se repite la ronda")
			else:
				self.sc2.send("Ingrese palabras correctas J2, piedra, papel o tijeras")
		elif tiroJug1=="tijeras":
			if tiroJug2=="papel":
				self.sc1.send("J1")
				self.sc1.send("   ")
				self.imprimeTijeras(self.sc1)
				self.sc2.send("J1")
				self.sc2.send("   ")
				self.imprimeTijeras(self.sc2)
				self.sc1.send("J2")
				self.sc1.send("   ")
				self.imprimePapel(self.sc1)
				self.sc2.send("J2")
				self.sc2.send("   ")
				self.imprimePapel(self.sc2)
				self.sc1.send("Ronda para jugador 1")
				self.sc2.send("Ronda para jugador 1")
				self.listaTablero2[r]="Perdida"
				self.listaTablero1[r]="Ganada"
				self.ganadasj1+=1
				# aqui se anadira a tabla
			elif tiroJug2=="piedra":
				self.sc1.send("J1")
				self.sc1.send("   ")
				self.imprimeTijeras(self.sc1)
				self.sc2.send("J1")
				self.sc2.send("   ")
				self.imprimeTijeras(self.sc2)
				self.sc1.send("J2")
				self.sc1.send("   ")
				self.imprimePiedra(self.sc1)
				self.sc2.send("J2")
				self.sc2.send("   ")
				self.imprimePiedra(self.sc2)
				self.sc1.send("Ronda para jugador 2")
				self.sc2.send("Ronda para jugador 2")
				self.listaTablero1[r]="Perdida"
				self.listaTablero2[r]="Ganada"
				self.ganadasj2+=1
				# aqui se anadira a tabla
			elif tiroJug2=="tijeras":
				self.sc1.send("J1")
				self.sc1.send("   ")
				self.imprimeTijeras(self.sc1)
				self.sc2.send("J1")
				self.sc2.send("   ")
				self.imprimeTijeras(self.sc2)
				self.sc1.send("J2")
				self.sc1.send("   ")
				self.imprimeTijeras(self.sc1)
				self.sc2.send("J2")
				self.sc2.send("   ")
				self.imprimeTijeras(self.sc2)
				self.sc2.send( "Empate, se repite la ronda")
				self.sc1.send( "Empate, se repite la ronda")
			else:
				self.sc2.send("Ingrese palabras correctas J2, piedra, papel o tijeras")
		elif tiroJug1=="papel":
			if tiroJug2 == "tijeras":
				self.sc1.send("J1")
				self.sc1.send("   ")
				self.imprimePapel(self.sc1)
				self.sc2.send("J1")
				self.sc2.send("   ")
				self.imprimePapel(self.sc2)
				self.sc1.send("J2")
				self.sc1.send("   ")
				self.imprimeTijeras(self.sc1)
				self.sc2.send("J2")
				self.sc2.send("   ")
				self.imprimeTijeras(self.sc2)
				self.sc1.send("Ronda para jugador 2")
				self.sc2.send("Ronda para jugador 2")
				self.listaTablero1[r]="Perdida"
				self.listaTablero2[r]="Ganada"
				self.ganadasj2+=1
				# aqui se anadira a tabla
			elif tiroJug2=="papel":
				self.sc1.send("J1")
				self.sc1.send("   ")
				self.imprimePapel(self.sc1)
				self.sc2.send("J1")
				self.sc2.send("   ")
				self.imprimePapel(self.sc2)
				self.sc1.send("J2")
				self.sc1.send("   ")
				self.imprimePapel(self.sc1)
				self.sc2.send("J2")
				self.sc2.send("   ")
				self.imprimePapel(self.sc2)
				self.sc2.send( "Empate, se repite la ronda")
				self.sc1.send( "Empate, se repite la ronda")
				
				# aqui se anadira a tabla
			elif tiroJug2=="piedra":
				self.sc1.send("J1")
				self.sc1.send("   ")
				self.imprimePapel(self.sc1)
				self.sc2.send("J1")
				self.sc2.send("   ")
				self.imprimePapel(self.sc2)
				self.sc1.send("J2")
				self.sc1.send("   ")
				self.imprimePiedra(self.sc1)
				self.sc2.send("J2")
				self.sc2.send("   ")
				self.imprimePiedra(self.sc2)
				self.send("Ronda para jugador 1")
				self.send("Ronda para jugador 1")
				self.listaTablero2[r]="Perdida"
				self.listaTablero1[r]="Ganada"
				self.ganadasj2+=1
			else:
				
				self.sc2.send("Ingrese palabras correctas J2, piedra, papel o tijeras")
		else:
			self.sc1.send("Ingrese palabras correctas J1, piedra, papel o tijeras")
			
				

	def torneo(self):
		for x in range(0, self.numeroPartidas):
			if(self.ganadasj2>(self.numeroPartidas/2)):
				self.sc1.send( "Jugador 2 GANA ")	
				self.sc2.send( "Jugador 2 GANA ")
				break
			elif(self.ganadasj1>(self.numeroPartidas/2)):
				self.sc1.send( "Jugador 1 GANA ")
				self.sc2.send( "Jugador 1 GANA ")
				break
			self.sc1.send("ronda")
			self.sc2.send("ronda")
			tiroJug1=self.sc1.rcv(1024)
			tiroJug2=self.sc2.rcv(1024)
			self.jugarDos(tiroJug1, tiroJug2, x)
			if(x<(self.ganadasj1+self.ganadasj2)):
				x=x-1
			self.mostrarTabla()
		
	def mostrarTabla(self):
		for x in range (0, self.numeroPartidas):
			self.sc1.send( self.listaTablero1[x] +"   " +self.listaTablero2[x])
			self.sc1.send(" ")
			self.sc2.send( self.listaTablero1[x] +"   " +self.listaTablero2[x])
			self.sc2.send(" ")
				

	
if __name__ == '__main__':
	cachipun=Cachipun(3)
	cachipun.torneo()
