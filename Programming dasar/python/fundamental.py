
# disini saya akan belajar dasar - dasar pemrogramman python 
# materi                        praktek
# 1. hello world!               tampilkan nama anda
# 2. variable dan tipe data     buat variable nama, umur, status, dll
# 3. operator                   buat program sederhana menghitung luas persegi dan cek apakah angka pertama lebih besar dari yang lain

print("Hello World!")
print("hallo selamat pagi mukhbit")
print('hai saya coba gaya baru dengan kutip satu')

# input dan output dasar
nama = input("Masukkan nama anda : ")
print("Hallo,", nama)

# struktur program dengan fungsi main
def main():
   print("Hello dari fungsi main!")

if __name__ == "__main__":
   main()


# tipe data dasar python
# integer
umur = 28
print(type(umur))

# float
tinggi = 173.5
print(type(tinggi))

# string
nama = "sulis"
print(type(nama))

# boolean
is_active = True
print(type(is_active))

# list
# list bersifat mutable (bisa diubah)
buah = ["appel", "jeruk", "mangga"]
print(type(buah))

# tuple
# tuple bersifat immutable (tidak bisa diubah)
warna = ("merah", "biru", "kuning")
print(type(warna))

# dictionary
# dict menyimpan data dalam bentuk pasangan ( key - value )
mahasiswa = {"nama":"budi", "umur":21, "alamat":"pesanggrahan"}
print(type(mahasiswa))

# set
# set berbentuk unik tidak ada duplikasi
angka = {1,2,3,4,5,'a','b','c'}
print(angka)
print(type(angka))

# variable
# aturan penamaan variable :
# 1. nama variable hanya boleh berisis huruf, angka dan underscore
# 2. variable tidak boleh diawali dengan angka
# 3. tidak boleh menggunakan keyword python seperti ( if, while, for, class dll)
# 4. penulisan nama variable menggunakan gaya snake_case
# contoh
# 1nama = "salah"
# class = "tkj"

nama = "andi"
umur = 25
tinggi = 170.5
status = True

# python juga mendukung pemberian nilai ke beberapa variable sekaligus
a, b, c = 12,23,43
# atau
x=y=z=100
print(x,y,z)
print(a,b,c)

print(nama)
print(umur)
print(tinggi)
print(status)

# untuk menghapus variable gunakan del
r = 10
print(r)

del r #otomatis variable r tehapus bersama nilainya

# contoh kasus ( praktek )
# disini membuat inputan untuk isi biodata pribadi karyawan
nama = input("Nama lengkap    : ")
umur = input("Umur            : ")
tinggi_badan = input("Tinggi  : ")
status = input("Status        : ")
hobi = input("Hobi            : ")

print("Nama lengkap  :", nama)
print("Umur          :", umur)
print("tinggi badan  :", tinggi)
print("Status aktif  :", status)
print("Hobi          :", hobi)


# operator
# nilai konstanta
# semua huruf kapital dan menggunakan uppercase
TAX_RATE = 0.1

harga_barang = 50000
total = harga_barang + (harga_barang * TAX_RATE)

print ("Total harga :", total)


# Operator 
# operator aritmatika
a = 10
b = 3

print(a - b)
print(a + b)
print(a * b)
print(a / b)
print(a // b) #pembagian bulat
print(a % b) #modulus
print(a ** b) #pangkat

# operator perbandingan
# oerator ini digunakan untuk membandingkan 2 nilai yang berbeda dan menghasilkan nilai True atau False
x = 5
y = 11

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# operator logika
a = True
b = False

print(a and b)
print(a or b)
print(not a)

# operator penugasan
x = 10
x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x /= 4
print(x)


# operator keanggotaan
buah = ["apel", "jeruk", "mangga"]

print("apel" in buah)      # True mencek apakah nilai ada dalam koleksi list
print("pisang" not in buah) # True mencek apakah nilai tidak ada dalam koleksi list

# operator identitas
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     # True (b menunjuk objek yang sama dengan a)
print(a is c)     # False (c objek berbeda walau isinya sama)
print(a == c)     # True (nilai isinya sama)

nama = input("nama panggilan : ")
print(f"Hallo, {nama}") # "f-string". Ini cara penulisan string yang lebih mudah dibaca di Python.
