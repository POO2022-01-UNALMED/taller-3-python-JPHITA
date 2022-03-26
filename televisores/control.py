class Control:
  
  def __init__(self):
    self._tv: TV = None

  def turnOn(self):
    self._tv.turnOn()
  
  def turnOff(self):
    self._tv.turnOff()

  def canalUp(self, canal = 1):
    if self._tv.getEstado() == True and (self._tv.getCanal() + canal) in (1,120):
      self._tv.canalUp(canal)
  
  def canalDown(self, canal = 1):
    if self._tv.getEstado() == True and (self._tv.getCanal() + canal) in (1, 120):
      self._tv.canalDown(canal)

  def setCanal(self, canal):
    self._tv.setCanal(canal)

  def volumenUp(self, vol = 1):
    if self._tv.getEstado() == True and (self._tv.getVolumen() + vol) in (0, 7):
      self._tv.volumenUp(vol)

  def volumenDown(self, vol = 1):
    if self._tv.getEstado() == True and (self._tv.getVolumen() + vol) in (0, 7):
      self._tv.volumenDown(vol)

  def enlazar(self, tv):
    self._tv = tv
    self._tv.setControl(self)

  def getTv(self):
    return self._tv
    
  def setTv(self, tv):
    self._tv = tv