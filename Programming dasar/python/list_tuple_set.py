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

# slicing = mengambil beberapa element sekaligus
buah = ["apel", "anggur", "pisang", "semangka"]
print(buah[1:3]) # ambil data dari mulai urut 1 sampai 3
print(buah[:2]) # ambil data di bawah urut 2
print(buah[2:]) #ambil data diatas urut 2

# method pop(): Mirip remove(), tapi pop(index) menghapus berdasarkan posisi (index) dan mengembalikan elemen yang dihapus.
buah_yang_dihapus = buah.pop(1) # Menghapus 'anggur'
print(f"Buah yang dihapus: {buah_yang_dihapus}")
print(f"List sekarang: {buah}")

# List Comprehension: Cara yang lebih singkat dan "keren" untuk membuat list baru dari list yang sudah ada.
# Cara lama
angka = [1, 2, 3, 4, 5]
angka_kuadrat = []
for a in angka:
   angka_kuadrat.append(a * a)

# Cara List Comprehension
angka_kuadrat_baru = [a * a for a in angka]
print(angka_kuadrat_baru) # Output: [1, 4, 9, 16, 25]



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

# Unpacking: Sangat berguna untuk menukar nilai atau memisahkan elemen
koordinat = (10, 20)
x, y = koordinat # x jadi 10, y jadi 20
print(f"x={x}, y={y}")

# Menukar nilai tanpa variabel bantuan
a, b = 100, 200
a, b = b, a # Sekarang a=200, b=100
print(a, b)

# Kapan Pakai Tuple? Gunakan tuple ketika data Anda tidak boleh berubah secara tidak sengaja. Contoh: koordinat, hari dalam seminggu, atau nilai kembalian dari sebuah fungsi yang lebih dari satu.
def hitung_statistik(data):
   return min(data), max(data) # Mengembalikan tuple

nilai_min, nilai_max = hitung_statistik([10, 5, 20, 15])



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

# .remove() vs .discard():
# set.remove(item): Akan menyebabkan KeyError jika item tidak ada.
# set.discard(item): Tidak akan error jika item tidak ada. Ini lebih aman.
angka = {1, 2, 3}
angka.discard(99) # Aman, tidak terjadi apa-apa
# angka.remove(99) # Akan menyebabkan error!

