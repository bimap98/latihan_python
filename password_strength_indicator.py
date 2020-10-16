a = input("Masukan password :")
if a.isdigit and len(a) <= 8:
    print("Password anda sangat lemah")
elif a.isalpha() and len(a) <= 8:
    print("Password anda lemah")
elif a.isalnum() and len(a) >= 8:
    print("Password anda kuat")
else:
    print("Password anda sangat kuat")
