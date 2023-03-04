#cara membuat class
class MobilAn:
    
    def __init__(self,brand,harga): #(__init__ = method)
        self.brand = brand
        self.harga = harga
#kendaraan1 = objek (object) ; Mobil(‘TOYOTA’,1000) = kelas (class)
kendaraan1 = MobilAn('TOYOTA',500)
print(kendaraan1.brand)
print(kendaraan1.harga)

kendaraan2 = MobilAn('MITSUBISHI',1000)
print(kendaraan2.brand)
print(kendaraan2.harga)

kendaraan3 = MobilAn('BMW',12000)
print(kendaraan3.brand)
print(kendaraan3.harga)
print("=================================================");
print("=================================================");
class Buah:
    penjual = 'Pak Imron' # ini class object attribute
    def __init__(self,nama_buah,harga):
        self.nama_buah = nama_buah
        self.harga = harga
    jenis_buah = 'Pisang Ambon' #ini class object attribute
fruit1 = Buah('Pisang',10000)
print('Nama buah =',fruit1.nama_buah)
print('Harga buah =',fruit1.harga)
print('Nama penjual buah =',fruit1.penjual)
print('Jenis Pisang =',fruit1.jenis_buah)
print("=================================================");
print("=================================================");
class Mobil:
    def __init__(self,brand,harga): #(__init__ = method)
        self.brand = brand
        self.harga = harga
        self.kondisi = 'baru'
        self.pemakaian = '3 tahun'
kendaraan1 = Mobil('TOYOTA',500) #bagian ini wajib didefinsikan
print('Brand =',kendaraan1.brand)
print('Price =',kendaraan1.harga)
print('Kondisi =',kendaraan1.kondisi)
print('Pemakaian =',kendaraan1.pemakaian)
print("=================================================");
print("=================================================");
#cara mengakses atribut
class Karyawan():
    jumlah_karyawan=0
    def __init__(self,nama,jobdesk,lama_bekerja):
        self.nama = nama
        self.jobdesk = jobdesk
        self.lama_bekerja = lama_bekerja
        Karyawan.jumlah_karyawan +=1
    def total_karyawan(self):
        print('Total Karyawan =', Karyawan.jumlah_karyawan)
    def detail_karyawan(self):
        print('Nama karyawan :', self.nama)
        print('Jobdesk karyawan :', self.jobdesk)
        print('Lama bekerja :', self.lama_bekerja)

# membuat objek
karyawan1 = Karyawan ('Aul', 'sales', '2 bulan')
karyawan2 = Karyawan ('Sabrina', 'kadiv HR','2 tahun')
karyawan3 = Karyawan ('Firna', 'Marketing', '10 bulan')
karyawan4 = Karyawan ('Zuhri', 'Manager', '4 tahun')
karyawan5 = Karyawan ('Diva', 'Sekretaris', '5 tahun')

# mengakses attribut objek
karyawan1.detail_karyawan()
karyawan2.detail_karyawan()
karyawan3.detail_karyawan()
karyawan4.detail_karyawan()
karyawan5.detail_karyawan()
Karyawan.total_karyawan(Karyawan)
