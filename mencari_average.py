inputan = input("Masukan list angka: ") #mencari average
keluar = inputan.split()
# print(keluar)
konvert = list(map(int, keluar))
print(sum(konvert)/len(konvert))
