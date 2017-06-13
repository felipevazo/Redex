class Rueda():
  def __init__(self,Color,Marca):
    self.Color=Color
    self.Marca=Marca
  def girar(self):
    print "Estoy girando"
class Auto():
  def __init__(self,Rueda1,Marca):
    self.Rueda1=Rueda1
    self.Rueda2=Rueda2
    self.Rueda3=Rueda3
    self.Rueda4=Rueda4
    self.Marca=Marca
  def acelerar(self):
    print "Auto Acelerando"
    
class Persona():
  def __init__(self):
    self.Nombre="Felipe"
    self.Auto=Auto(Rueda("Roja","Michelin"),"Toyota")
    Auto.acelerar()
