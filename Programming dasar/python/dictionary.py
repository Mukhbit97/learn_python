
# dictionary
# dictionary terdiri dari key dan value
# membuat dictionary
mahasiswa = {
   "nama": "budi",
   "umur": 20,
   "jurusan": "informatika"
}

print(mahasiswa)

# mengakses data
print(mahasiswa["nama"])
print(mahasiswa.get("umur")) #jika menggunakan get maka key tidak akan mengembalikan error / none

# menambah data
mahasiswa["angkatan"] = 2023
print(mahasiswa)

# mengubah data
mahasiswa["umur"] = 21
print(mahasiswa)

# menghapus data
mahasiswa.pop("jurusan")
del mahasiswa["nama"]
print(mahasiswa)

# iterasi dictionary
for key, value in mahasiswa.items():
   print(key, ":", value)

# nested dictionary
kampus = {
   "mahasiswa1" : {"nama": "budi", "umur":20},
   "mahasiswa2" : {"nama": "siti", "umur":23}
}
print(kampus["mahasiswa1"]["nama"])