a = int(input("Masukan harga barang: Rp "))
b = float(input("Mau diskon berapa? Contoh inputan 3% = 0.03 , 30% = 0.30 , 100% = 1.00  : "))
print("Harga barang sebesar","{}".format(a),"dengan diskon","{}".format(b*100),"%","maka harganya jadi Rp",a-(a*b))
