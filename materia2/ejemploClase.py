class Holamundo(): # creando clases en python
	def__init__(self): # En todos los metodos debe estar el SELF!, aparte self-> this
		self.texto="Hola Mundo"
	def mostrar(self,nombre):
		self.nombre=nombre
		print self.texto, self.nombre
		self.blabla()
	def blabla(self):
		print self.nombre


# fin de la clase

nombre=raw_imput("Ingrese su nombre: ")
hola=Holamundo()
print hola.texto
hola.mostrar(nombre)
