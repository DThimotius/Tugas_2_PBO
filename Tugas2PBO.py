class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("=====================================")
        print(" Daftar Mahasiswa", self.NamaJurusan)
        print("-------------------------------------")
        print(" Nama     : ", self.nama)
        print(" NIM      : ", self.nim)
        print(" Jurusan  : ", self.NamaJurusan)
        print("-------------------------------------")
        print("=====================================")
"""
*Kelas Mahasiswa mendefinisikan sebuah class bernama Mahasiswa
*Objek yang dibuat dari class Mahasiswa akan memiliki atribut nama, nim, dan jurusan yang nilainya diambil dari parameter yang diberikan.
*Metode tampilkan_info digunakan untuk menampilkan informasi mahasiswa yang mencakup nama, nim, dan jurusan.
"""

class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []
    
    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)
    
    def tampilkan_daftar_mahasiswa(self):
        print("=====================================")
        print(" Daftar Mahasiswa", self.NamaJurusan)
        print("-------------------------------------")
        for mahasiswa in self.DaftarMahasiswa:
            print(" Nama     : ", mahasiswa.nama)
            print(" NIM      : ", mahasiswa.nim)
            print(" Jurusan  : ", self.NamaJurusan)
            print("-------------------------------------")
        print("=====================================")
"""
*Kelas Jurusan mendefinisikan sebuah class bernama Jurusan.
*Objek yang dibuat dari class Jurusan akan memiliki atribut NamaJurusan yang nilainya diambil dari parameter yang diberikan.
*Atribut DaftarMahasiswa adalah sebuah list yang digunakan untuk menyimpan objek mahasiswa.
*Metode tambah_mahasiswa digunakan untuk menambahkan objek mahasiswa ke dalam atribut DaftarMahasiswa.
*Metode tampilkan_daftar_mahasiswa digunakan untuk menampilkan daftar mahasiswa yang terdaftar dalam jurusan.
"""

class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []
    
    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)
    
    def tampilkan_daftar_jurusan(self):
        print("=====================================")
        print("    Daftar Jurusan", self.NamaUniversitas)
        print("-------------------------------------")
        for jurusan in self.DaftarJurusan:
            print(" Nama Jurusan   :", jurusan.NamaJurusan)
            print("-------------------------------------")
        print("=====================================")
"""
*Kelas Universitas mendefinisikan sebuah class bernama Universitas.
*Objek yang dibuat dari class Universitas akan memiliki atribut NamaUniversitas yang nilainya diambil dari parameter yang diberikan.
*Atribut DaftarJurusan adalah sebuah list yang digunakan untuk menyimpan objek jurusan.
*Metode tambah_jurusan digunakan untuk menambahkan objek jurusan ke dalam atribut DaftarJurusan.
*Metode tampilkan_daftar_jurusan digunakan untuk menampilkan daftar jurusan yang ada di universitas.      
"""
universitas_xyz = Universitas("XYZ University")
#Membuat object universitas_xyz dari class Universitas dengan nama "XYZ University"

jurusan_TI = Jurusan("Teknik Informatika")
#Membuat object jurusan_TI dari class Jurusan dengan nama jurusan "Teknik Informatika"

universitas_xyz.tambah_jurusan(jurusan_TI) 
#Object jurusan ditambahkan ke dalam object universitas_xyz menggunakan metode tambah_jurusan

mahasiswa = Mahasiswa("David Thimotius Rarung", "G1A022045", jurusan_TI)
#Membuat mahasiswa dari class Mahasiswa dengan nama dan nim saya

jurusan_TI.tambah_mahasiswa(mahasiswa)
#Object mahasiswa ditambahkan ke dalam object jurusan_TI menggunakan metode tambah_mahasiswa

universitas_xyz.tampilkan_daftar_jurusan()
#Menampilkan daftar jurusan yang ada di Universitas

jurusan_TI.tampilkan_daftar_mahasiswa()
#Menampilkan daftar mahasiswa yang ada dalam jurusan_TI