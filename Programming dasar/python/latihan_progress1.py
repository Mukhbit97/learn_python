
# # Soal 1 Fungsi Matematika
# # buat sebuah fungsi bernama hitung_luas_persegi_panjang
# print("Program perhitungan luas persegi panjang")
# def hitung_luas_persegi_panjang(panjang, lebar):
#    return panjang * lebar
# try:
#    # input dari user
#    panjang = float(input("Masukkan Panjang Persegi :"))
#    lebar = float(input("Masukkan Lebar Persegi :"))

#    # panggil fungsi tanpa parameter
#    # hasil_perhitungan = hitung_luas_persegi_panjang()

#    # panggil fungsi dengan parameter
#    hasil_perhitungan = hitung_luas_persegi_panjang(panjang, lebar)
#    print(f"Hasil Hitung Luas Persegi Panjang = {hasil_perhitungan}")
# except ValueError:
#    print("input yang anda masukkan salah")
   
# # soal 2 fungsi dengan logika kondisional
# # buatlah fungsi cek_kelulusan dengan ketentuan jika nilai diatas 70 = lulus dan bila kurang dari 70 = tidak lulus
# print("program cek status kelulusan")
# # def cek_kelulusan(nilai):
# #    return nilai

# # try:
# #    nilai = int(input("Masukkan Nilai Ujian anda : "))
# #    if nilai > 70:
# #       print("Selamat anda lulus ujian")
# #    else:
# #       print("Maaf anda tidak lulus")
# # except ValueError:
#    # print("input yang anda masukkan salah")

# # perbaikan dari Ai
# print("program cek status kelulusan")

# #  1. pindahkan logika if/else ke dalam fungsi
# def cek_kelulusan(nilai):
#    if nilai > 70:
#       return "selamat anda lulus ujian"
#    else :
#       return "maaf anda tidak lulus"
# # 2. bagian utama program menjadi lebih bersih
# try:
#    nilai_input = int(input("masukkan nulai ujian anda :"))

#    # 3. cukup panggil fungsinya dan simpan hasilnya
#    status = cek_kelulusan(nilai_input)

#    # 4. tampilkan hasil yang sudah di kembalikan fungsi
#    print(status)

# except ValueError:
#    print("input yang anda masukan salah")

# # Soal 3 fungsi memproses data dalam list
# # buatlah fungsi cari_angka_terbesar dari list [3, 4, 9, 12, 5, 7, 1]
# print("program mencari angka terbesar dalam list")

# # def cari_angka_terbesar(data_list):
# #    nilai_terbesar = data_list[0]
# #    for angka in data_list:
# #       if angka > nilai_terbesar:
# #          nilai_terbesar = angka
# #    return nilai_terbesar

# # # data list
# # angka_list = [3, 4, 9, 12, 5, 7, 1]

# # # Panggil fungsi
# # hasil = cari_angka_terbesar(angka_list)
# # print(f"Nilai terbesar adalah: {hasil}")

# # perbaikan dari ai
# def cari_angka_terbesar(data_list):
#    # penanganan jika list kosong, agar tidak error
#    if not data_list:
#       return None
   
#    nilai_terbesar = data_list[0]
#    print(f"nilai awal : {nilai_terbesar}")

#    # mulai loop dari element ke dua (index 1) sampai akhir
#    for angka in data_list[1:]:
#       print(f"-> sedang memeriksa angka : {angka}")
#       if angka > nilai_terbesar:
#          nilai_terbesar = angka
#          print(f" ditemukan yang lebih besar! nilai terbesar di update menjadi : {nilai_terbesar}")
#       else:
#          print(f" {angka} tidak lebih besar dari {nilai_terbesar} lewat")

#    print("-" * 20)
#    return nilai_terbesar
# # data list
# angka_list = [3, 4, 9, 12, 5, 7, 1]

# # pamggilan fungsi debug
# hasil = cari_angka_terbesar(angka_list)
# print(f"nilai terbesar adalah : {hasil}")


# tugas akhir sistem manajemetn kontak sederhana
# buat program manajement kontak menggunakan fungsi 
# --- Definisi semua fungsi ---

def tambah_kontak(daftar_kontak):
   print("\n --- tambah kontak baru ---")
   try:
      nama = input("Masukkan Nama :")
      telepon = input("Masukkan nomor telepon :")
      
      # buat dictionary untuk kontak baru
      list_kontak = {'nama' : nama, 'telepon' : telepon}

      # tambahkan ke daftar kontak
      daftar_kontak.append(list_kontak)
      print(f"Kontak telah berhasil di tambahkan {nama}")
   except ValueError:
      print("harap input data dengan benar di tambah kontak")

def lihat_semua_kontak(daftar_kontak):
   if not daftar_kontak:
      print("daftar kosong")
   else:
      for i, kontak in enumerate (daftar_kontak):
         # enumerate untuk mendapatkan nomor urut
         print(f"{i+1}, nama : {kontak['nama']}, telepon : {kontak['telepon']}")
   print("-" * 20)

def cari_kontak(daftar_kontak):
   if not daftar_kontak:
      print("daftar kontak masih kosong")
      return
   
   cari_nama = input("masukkan nama yang dicari :")
   ditemukan = False

   for kontak in daftar_kontak:
      if kontak['nama'].lower() == cari_nama.lower():
         print(f"nama ditemukan {kontak['nama']} nomor telepon {kontak['telepon']}")
         ditemukan = True
         break
      
      if not ditemukan:
         print(f"nama {cari_nama} tidak ditemukan silahkan input data")

def hapus_kontak(daftar_kontak):
   print("\n--- Hapus Kontak ---")
   if not daftar_kontak:
      print("Daftar kontak masih kosong.")
      return

   nama_dicari = input("Masukkan nama kontak yang ingin dihapus: ")
   ditemukan = False

   # Gunakan enumerate untuk mendapatkan index dan item secara bersamaan
   for index, kontak in enumerate(daftar_kontak):
      if kontak['nama'].lower() == nama_dicari.lower():
         # Hapus kontak berdasarkan index-nya
         daftar_kontak.pop(index)
         print(f"Kontak '{nama_dicari}' berhasil dihapus.")
         ditemukan = True
         break # Keluar dari loop setelah menghapus

   if not ditemukan:
      print(f"Kontak dengan nama '{nama_dicari}' tidak ditemukan.")

def main():
   daftar_kontak = []
   
   while True:
      print("--- Pilihan Menu ---")
      print("1. tambah kontak")
      print("2. lihat daftar kontak")
      print("3. cari kontak")
      print("4. hapus kontak")
      print("5. keluar")

      try:
         perintah = int(input("masukkan pilhan anda :"))

         if perintah == 1:
            tambah_kontak(daftar_kontak)
         elif perintah == 2:
            lihat_semua_kontak(daftar_kontak)
         elif perintah == 3:
            cari_kontak(daftar_kontak)
         elif perintah == 4:
            hapus_kontak(daftar_kontak)
         else:
            print("terimakasih sampai jumpa")
            break
      except ValueError:
         print("input yang anda masukan tidak ada dalam daftar")
main()