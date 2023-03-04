print("Function Method" )
#menghapus semua item dari dictionary
worldcup= dict(
   nama_klub = ("Argentina","Portugal","Prancis","Maroko","Kroasia"),
   nama_pemain = ("Messi","Mbappe","Modric","Hakimi","Ramos"),
   pemain_terbaik = "Messi",
   pemain_terbaik = "Messi",
   pemain_terbaik = "Messi",
   pemain_terbaik = "Messi",
)
dict.clear(worldcup)
print(worldcup)
print("=========================================")
print("=========================================")
#menyalin dictionary  dengan metode copy()
dictionary1 = {
    "partai": "Banteng Merah",
    "slogan" : "3 priode atau tidak sama sekali !!! ",
}
dict2 = dictionary1.copy() 
print (dict2) 
print("=========================================")
print("=========================================")
print("=========================================")
 
#mengeluarkan item dictionary menjadi list
pemain = {
    'nama' : "Ronaldo",
    'hobi' : "duduk di bangku cadangan",
    'pencapaian world cup 22' : "pulang duluan"
}
print(pemain.items()) 
print("=========================================")
print("=========================================")
print("=========================================")
#mengembalikan daftar dari pasangan tuple
Indonesia = dict (
    Squad = ("firman utina","atep","markus","gonzalez"),
    jumlah = "23 orang",
    pelatih = "djajang nurjaman",
)
Indonesia.popitem()
print(Indonesia) 
print("=========================================")
print("=========================================")
print("=========================================")
#menampilkan semua key
Argentina = dict (
    pemainterbaik = "Acuna a.k.a deni",
    Prestasi = "juara world cup",
)
print(Argentina.keys())
print("=========================================")
print("=========================================")
print("=========================================")
#menampilkan semua value pada dictionary
Orang_Sakti = dict(
    nama = " Gus Samsudin",
    umur = "1001 tahun",
    quotes = "hooh tenanan",
)
print(Orang_Sakti.values())
print("=========================================")
print("=========================================")
print("=========================================")
#mengupdate value dari dictionary
Riza = {
    'nama': "vini",
    'umur': "19 tahun",
    'asal': "garut",
}
Riza.update({'nama':"Jihan"})
print(Riza)
print("=========================================")
print("=========================================")
print("=========================================")
print("Built In")
#menghitung panjang total dictionary
person = dict(
    nama = "aldi daim",
    umur = "20 tahun",
    kesibukan = "mengurus web sains data",
    asal = "cimahi",
    suka = "ngopi",
)
print(len(person))
print("=========================================")
print("=========================================")
print("=========================================")
#merepresentasikan string dari dictionary
Messi = dict(
    pencapaian2022= "juara world cup",
    balon_dor= "7 ballon d'or",
    klub = "PSG"
)
print(str(Messi))
print("=========================================")
print("=========================================")
print("=========================================")
#mengembalikan tipe variabel,contohnya "type"({})
# akan di kembalikan menjadi tipe data dictionary
Prodi = {
    'nama':"Sains Data",
    'jumlah mahasiswa' :"26 orang",
    'nama HIMA':"HIMASTA"
}
print(type(Prodi))



 
 
