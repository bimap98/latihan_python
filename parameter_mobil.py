class mobil:
    def __init__(self,warna,jenis,harga):
        self.warna = warna
        self.jenis = jenis
        self.harga = harga
    
    def tampil(self,mahal):
        if mahal:
            print("Mobil ini berwarna %s lalu jenis nya %s dengan harga %s" %(self.warna,self.jenis,self.harga))
        else:
            print("Belii dah mobil warna",self.warna)

a = mobil("Biru","Sedan",5000)
a.tampil(True)
a.tampil(False)
