class Cachipun():
	def __init__(self, numeroPartidas):
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

	def jugarDos(self, tiroJug1, tiroJug2,r):
		tiroJug1=tiroJug1.lower()
		tiroJug2=tiroJug2.lower()
		if tiroJug1 == "piedra":
			if tiroJug2=="papel":
				print "ronda para jugador 2"
				self.ganadasj2+=1
				self.listaTablero1[r]="Perdida"
				self.listaTablero2[r]="Ganada"
			elif tiroJug2=="tijeras":
				self.listaTablero2[r]="Perdida"
				self.listaTablero1[r]="Ganada"
				print "ronda para jugador 1"
				self.ganadasj1+=1
				# aqui se anadira a tabla
			elif tiroJug2=="piedra":
				print "empate, se repite la ronda"
			else:
				print "Ingrese palabras correctas J2, piedra, papel o tijeras"
		elif tiroJug1=="tijeras":
			if tiroJug2=="papel":
				print "ronda para jugador 1"
				self.listaTablero2[r]="Perdida"
				self.listaTablero1[r]="Ganada"
				self.ganadasj1+=1
				# aqui se anadira a tabla
			elif tiroJug2=="piedra":
				print "ronda para jugador 2"
				self.listaTablero1[r]="Perdida"
				self.listaTablero2[r]="Ganada"
				self.ganadasj2+=1
				# aqui se anadira a tabla
			elif tiroJug2=="tijeras":
				print "Empate, se repite la ronda"
			else:
				print "Ingrese palabras correctas J2, piedra, papel o tijeras"
		elif tiroJug1=="papel":
			if tiroJug2 == "tijeras":
				print "ronda para jugador 2"
				self.listaTablero1[r]="Perdida"
				self.listaTablero2[r]="Ganada"
				self.ganadasj2+=1
				# aqui se anadira a tabla
			elif tiroJug2=="papel":
				print "Empate, se repite la ronda"
				
				# aqui se anadira a tabla
			elif tiroJug2=="piedra":
				print "Ronda para jugador 1"
				self.listaTablero2[r]="Perdida"
				self.listaTablero1[r]="Ganada"
				self.ganadasj2+=1
			else:
				print "Ingrese palabras correctas J2, piedra, papel o tijeras"
		else:
			print "Ingrese palabras correctas J1, piedra, papel o tijeras"
				

	def torneo(self):
		for x in range(0, self.numeroPartidas):
			if(self.ganadasj2>(self.numeroPartidas/2)):
				print "Jugador 2 GANA "				
				break
			elif(self.ganadasj1>(self.numeroPartidas/2)):
				print "Jugador 1 GANA "
				break
			tiroJug1=raw_input("Tiro j1>>>")
			tiroJug2=raw_input("Tiro j2>>>")
			self.jugarDos(tiroJug1, tiroJug2, x)
			if(x<(self.ganadasj1+self.ganadasj2)):
				x=x-1
			self.mostrarTabla()
		
	def mostrarTabla(self):
		for x in range (0, self.numeroPartidas):
			print self.listaTablero1[x] +"   " +self.listaTablero2[x]
			print " "
				

	
if __name__ == '__main__':
	cachipun=Cachipun(3)
	cachipun.torneo()
	print "shao lo vimoh"	
