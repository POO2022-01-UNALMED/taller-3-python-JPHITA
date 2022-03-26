# modulo televisores

class TV:

  _numTV : int = 0

  def __init__(self, marca, estado):
      self._marca: Marca = marca
      self._canal: int = 1
      self._precio: int = 500
      self._estado: bool = estado
      self._volumen: int = 1
      self._control: Control = None

      _numTV += 1

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

  
