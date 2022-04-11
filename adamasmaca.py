# Adam Asmaca Oyunu
# Yazan : Seyfullah Polat
# Tarih : 09.04.2022
#Dahada Geliştirile Bilir Temel Seviyede Bir Oyun Kendinize Göre Ayarlıya bilirsiniz :) 

isim = input("Lütfen İsminizi Giriniz: ")
print("Merhaba " + isim + " Adam Asmaca Zamanı !!! ")

gizli_kelime = "adam"  #Buraya Kullanmak İstediğiniz Gizli Kelimeyi Gire Bilirsiniz.

tahmin_harf = ""

can = 10

while can > 0:

	harf_sayısı = 0

	for harf in gizli_kelime:

		if harf in tahmin_harf:
			print(harf)
		else:
			print("-")
			harf_sayısı += 1

	if harf_sayısı == 0:
		print("Tebrikler Adamı Kurtardın :) ")
		break


	tahmin = input("Bir Harf Tahmin Ediniz: ")
	tahmin_harf += tahmin

	if tahmin not in gizli_kelime:
		can -= 1
		print("Yanlış Tahmin Dostum :( ")
		print(f"Kalan Canın {can}")

		if can == 0:
			print("Malesef Kayettin :( ")