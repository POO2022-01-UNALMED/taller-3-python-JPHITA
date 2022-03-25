# modulo televisores

class Marca:

  def __init__(self, nombre):
    self._nombre = nombre

  def getnombre(self):
    return self._nombre

  def setnombre(self, nombre):
    self._nombre = nombre


class Control:
  
  def __init__(self):
    self._tv: TV = None

  def turnOn(self):
    self.tv.turnOn()
  
  def turnOff(self):
    self.tv.turnOff()

  def canalUp(self, canal = 1):
    if self.tv.getEstado() == True and (self.tv.getCanal() + canal) in (1,120):
      self.tv.canalUp(canal)
  
  def canalDown(self, canal = 1):
    if self.tv.getEstado() == True and (self.tv.getCanal() + canal) in (1, 120):
      self.tv.canalDown(canal)

  def setCanal(self, canal):
    self.tv.setCanal(canal)

  def volumenUp(self, vol = 1):
    if self.tv.getEstado() == True and (self.tv.getVolumen() + vol) in (0, 7):
      self.tv.volumenUp(vol)

  def volumenDown(self, vol = 1):
    if self.tv.getEstado() == True and (self.tv.getVolumen() + vol) in (0, 7):
      self.tv.volumenDown(vol)

  def enlazar(self, tv):
    self._tv = tv
    self._tv.setControl(self)

  def getTv(self):
    return self._tv
    
  def setTv(self, tv):
    self._tv = tv




class TV:

  _numTV : int = 0

  def __init__(self, marca, estado):
      self._marca: Marca = marca
      self._canal: int = 1
      self._precio: int = 500
      self._estado: bool = estado
      self._volumen: int = 1
      self._control: Control = None

  def getMarca(self):
    return self._marca
  
  def setMarca(self, marca):
    self._marca = marca

  def getControl(self):
    return self._control

  def setControl(self, control):
    self._control = control
  
  def getPrecio(self):
    return self._precio

  def setPrecio(self, precio):
    self._precio = precio

  def getVolumen(self):
    return self._volumen

  def setVolumen(self, volumen):
    self._volumen = volumen

  def getCanal(self):
    return self._canal
  
  def setCanal(self, canal):
    self._canal = canal

  @classmethod
  def getNumTV(cls):
    return cls._numTV

  @classmethod
  def setNumTV(cls, numTV):
    cls._numTV = numTV

  def turnOn(self):
    self._estado = True
  
  def turnOff(self):
    self._estado = False
  
  def getEstado(self):
    return self._estado

  def canalUp(self, canal = 1):
    if self._estado == True and (self._canal + canal) in (1,120):
      self._canal += canal
  
  def canalDown(self, canal = 1):
    if self._estado == True and (self._canal + canal) in (1, 120):
      self._canal -= canal

  def volumenUp(self, vol = 1):
    if self._estado == True and (self._volumen + vol) in (0, 7):
      self._volumen += vol

  def volumenDown(self, vol = 1):
    if self._estado == True and (self._volumen + vol) in (0, 7):
      self._volumen -= vol

  
