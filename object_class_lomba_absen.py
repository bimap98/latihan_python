class mahasiswa:

    def __init__(self, nama, kelas, absen, jenis_kelamin):
        self.name = nama
        self.ke_las = kelas
        self.absensi = absen
        self.gender = jenis_kelamin
    
    def lomba(self):
        print("Selanjutnya nama",self.name,"dari kelas",self.ke_las,"dan jenis kelamin",self.gender)
    
    def absen(self):
        print("Dipanggil",self.name,"dari kelas",self.ke_las,"dengan absen",self.absensi)
a = mahasiswa("welly","b",1,"pria")
a.lomba()
a.absen()
print(a)
