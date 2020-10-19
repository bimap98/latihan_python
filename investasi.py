a = int(input("Masukan jumlah dana: "))
b = float(input("Masukan presentase dalam persen: "))
c = int(input("Masukan tahun ke berapa? "))
d = (int(a)*b)/100
naik = c*d
total = a + naik

print("Pada tahun ke {}".format(c), "dengan kenaikan {}".format(b), "investasi nya akan menghasilkan {}".format(total))
