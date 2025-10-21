
# disini saya akan belajar dasar - dasar pemrogramman python 
# materi                        praktek
# 1. if/elif/else                Buat program yang meminta input umur. Jika < 17, cetak "Anda belum cukup umur". Jika 17-60, cetak "Anda dewasa". Jika > 60, cetak "Anda senior". 
#                                Mintai input sebuah angka. Cek apakah angka itu positif, negatif, atau nol, lalu cetak hasilnya.
# 2. Loops (for & while)         For Loop: Buat sebuah list buah-buahan. Gunakan for loop untuk mencetak setiap nama buah dalam list tersebut dengan kalimat "Saya suka makan [nama buah]". 
#                                While Loop: Buat program tebak angka. Simpan sebuah angka rahasia (misalnya angka_rahasia = 7). Gunakan while True untuk terus meminta user menebak angka. Jika tebakan benar, cetak "Tebakan Anda benar!" dan hentikan loop dengan break. Jika salah, beri petunjuk "Terlalu besar" atau "Terlalu kecil".

# percabangan 
nilai = int(input("Masukkan Nilai Siswa :")) # untuk memasukkan input berupa integer

if nilai >= 90:
   print("A")
elif nilai >= 75:
   print("B")
else:
   print("C")

# penggunaan error handling dengan try catch / try exception
try:
   umur = int(input("Masukkan Umur anda :"))

   if umur <= 17:
      print("Masih Anak - Anak")
   elif umur >= 15 and umur <= 29:
      print("Anak Muda")
   else:
      print("Sudah Tua")
except ValueError:
   print("Input yang anda masukan salah, Harap masukkan angka!")

try:
   angka = float(input("Masukkan angka anda :"))

   if angka > 0:
      print("Angka yang anda Masukan bernilai Positif")
   elif angka < 0:
      print("Angka yang anda masukkan bernilai Negatif")
   else:
      print("Angka anda Nol")
except ValueError:
   print("Input yang anda masukkan bukan angka.")


# perulangan For
buah = ["apel", "jeruk", "mangga"]

for item in buah:
   print(f"saya suka makan, {buah[1]}")
   break

for i in range(1, 6):
   if i == 3:
      continue
   if i == 5:
      break
   print(i)

# perulangan while
count = 0

while count < 5:
   print(f"Hitung : {count}")
   count += 1

angka_rahasia = 7
print(f"Ada angka rahasia disini antara 1 sampai 10 coba tebak !")

while True:
   try:
      tebakan = int(input("Masukakan angka tebakanmu :"))

      if tebakan > angka_rahasia:
         print("angka terlalu besar, coba lagi")
      elif tebakan < angka_rahasia:
         print("angka lebih kecil, coba lagi")
      else:
         print("tebakan benar, selamat")
         break
   except ValueError:
      print("yang anda input bukan angka")
