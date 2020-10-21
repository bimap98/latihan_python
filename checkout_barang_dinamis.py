import time
start = time.time()

total = 0
antrian = 0
pengulangan = 2

for a in range(pengulangan):
    antrian = antrian+1

    harga = input("Masukan harga: ")
    jumlah = input("Masukan jumlah: ")

    print("Harga barang ke {}: Rp.".format(antrian) +harga)

    print("Jumlah barang ke {}: ".format(antrian) +jumlah)

    total_harga = int(harga) * int(jumlah)
    total = total + total_harga
    

pajak = (float(total)*5.5)/100
total_keseluruhan = total + pajak

print("----------")
print("Harga keseluruhan: Rp.",total_harga)
print("Pajak: Rp.",pajak)
print("Harga keseluruhan + pajak: Rp.",total_keseluruhan+pajak)
end = time.time()
print(f"Runtime of the program is {end - start}")
