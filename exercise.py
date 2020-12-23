# odev3 exercise

dogruSayisi = int(input("Ogrencinin dogru sayisini girin: "))
yanlisSayisi = int(input("Ogrencinin yanlis sayisini girin: "))


class Ogrenci():
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinifi = ogrenciSinifi


class Soru():
    def NetSayisi(self, dogruSayisi, yanlisSayisi):
        net = dogruSayisi - (yanlisSayisi / 4)
        return net

    def Hesapla(self, net):
        puan = net * 2
        return puan


ogrenciBilgileri = Ogrenci("Ahmet", "Kaya", "5-A")
soru = Soru()
print("ad soyad: " + ogrenciBilgileri.ogrenciAdi,
      ogrenciBilgileri.ogrenciSoyadi + "\n" + "sınıfı: " + ogrenciBilgileri.ogrenciSinifi + "\n" + "ogrencinin neti: " + str(soru.NetSayisi(
          dogruSayisi, yanlisSayisi)) + "\n" + "ogrencinin puani: " + str(soru.Hesapla(
          soru.NetSayisi(dogruSayisi, yanlisSayisi))))
