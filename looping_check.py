buah = ['Nanas','Semangka','Melon',"Salak",3,7,9,4]
for a in buah:
    if a == "Melon":
        print("Ada melon")
    else:
        print("Tidak ada melon")    

print(40*"#")

for b in range(0,8):
    if buah[b] == "Melon":
        print("Ada melon")
    else:
        print("Tidak ada melon")

print(40*"$")

for b in range(len(buah)):
    if buah[b] == "Melon":
        print("Ada melon")
    else:
        print("Tidak ada melon")

