# list 
# ialah struktur data yang bersifat mutable ( datap diubah ) mendukung elemen duplikat, dan urutannya terjaga

# membuat lsit buah
buah = ["apple", "jeruk", "mangga"]

# akses element
print(buah[0])

# update element
buah[1] = "anggur"

# hapus element
buah.remove("mangga")

# menambah element
buah.append("pisang")

print(buah)


# tuple
# mirip dengan list namun bersifat immutable (tidak dapat diubah)
# membuat tuple
warna = ("merah", "hijau", "biru")

# akses element
print(warna[1])

# tuple tidak dapat diubah
# warna[0] = "kuning" 

# akses element dengan loop
for w in warna:
   print(w)


# set
# set bersifat unik ( tidak ada duplikat ) dan tidak berurutan
# membuat set
angka = {1,2,3,4,5,3,4,5}

print(angka) # duplikat otomatis hilang

# menambah element
angka.add(6)

# menghapus element
angka.remove(2)

print(angka)

# operasi himpunan
ganjil = {1,3,5,7}
genap = {2,4,6,8}

print(ganjil | genap) # union
print(ganjil & genap) # intersection (irisan)
print(ganjil - genap) # difference (selisih) / element yang tidak ada di element yang satunya

