class Holamundo(): # creando clases en python
	def__init__(self):
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
