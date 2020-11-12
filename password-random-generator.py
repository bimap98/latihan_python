import random

list_ku = "1234567890abcdefghijklmnoqrsqwxyzABCDEFGHIJKLMNOQRSQWXYZ"
panjang_text = int(input("Masukan panjang teks: "))
print("".join(random.sample(list_ku,panjang_text)))

