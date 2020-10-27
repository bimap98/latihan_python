baca = open("contoh.txt","r")
baca_file = baca.readlines()

baris = []
# for a in baca_file: #manual
#     if a[-1] == "\n":
#         baris.append(a[:-1])
#     else:
#         baris.append(a)
# print(baris)        
print(20*"#")
for a in baca_file: #otomatis
    baris.append(a.strip())
print(baris)
