class kisi:
  def __init__(self,ad,soyad):
    self.ad=ad
    self.soyad=soyad
  def karsilama(self):
    print("hoş geldin, ",self.ad)
  def ugurlama(self):
    print("güle güle, ",self.ad)
   

kisi1=kisi("mehmet",34)
kisi1.karsilama()
kisi1.ugurlama()
