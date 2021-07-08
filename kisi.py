class kisi:
  def __init__(self,ad,soyad,yas):
    self.ad=ad
    self.soyad=soyad
    self.yas=yas
  def karsilama(self):
    print("hoş geldin, ",self.ad,self.soyad)
    print("yaşın: ",self.yas)
  def ugurlama(self):
    print("güle güle, ",self.ad)
   

kisi1=kisi("mehmet","beyazgül",34)
kisi1.karsilama()
kisi1.ugurlama()
