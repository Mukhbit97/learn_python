
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

# Method .keys(), .values(), .items():
# Anda sudah pakai .items() di loop. Tahu saja Anda bisa mendapatkan semua key atau semua value saja.
mahasiswa = {"nama": "budi", "umur": 20}
print(mahasiswa.keys())   # Output: dict_keys(['nama', 'umur'])
print(mahasiswa.values()) # Output: dict_values(['budi', 20])

# Dictionary Comprehension: Sama seperti list, tapi untuk dictionary.
angka = [1, 2, 3, 4]
kuadrat_dict = {a: a*a for a in angka}
print(kuadrat_dict) # Output: {1: 1, 2: 4, 3: 9, 4: 16}