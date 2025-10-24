
# inventory = {
#    "LPT001": {"nama": "Laptop ASUS", "stok": 10, "harga": 15000000, "kategori": "Elektronik"},
#    "PKT001": {"nama": "Paket Indomie", "stok": 50, "harga": 13000, "kategori": "Makanan"}
# }

# riwayat = [
#    {"tipe": "jual", "sku": "LPT001", "Jumlah": 2, "waktu": "2023-10-27 10:00"},
#    {"tipe": "tambah_stok", "sku": "PKT001", "jumlah": 20, "waktu": "2023-10-27 11:00"}
# ]

# # Menggunakan set comprehension untuk mengambil semua kategori unik
# set_kategori = {item['tipe'] for item in riwayat}

# # Menampilkan hasilnya
# print(set_kategori)

# Data awal
inventory = {}
kategori = set()
riwayat =[]

def tambah_barang(inventory, kategori):
   # 1. Minta input SKU, nama, stok, harga, kategori
   # 2. Tambahkan data baru ke dictionary `inventory`
   #    inventory[sku] = {"nama": ..., "stok": ..., dst}
   # 3. Tambahkan kategori baru ke `set kategori`
   # 4. Beri konfirmasi bahwa barang berhasil ditambahkan

   print("\n --- tambah barang inventory ---")
   try:
      sku = input("Masukkan sku barang : ")
      nama = input("Masukkan nama barang : ")
      stok = int(input("masukkan stok barang : "))
      harga = float(input("masukkan harga barang : "))
      kategory = input("masukkan kategori barang : ")
      kategori.add(kategory)

      inventory[sku] = {
         "nama":nama, 
         "stok":stok, 
         "harga":harga, 
         "kategori":kategory
         }
      print(f"\nBarang '{nama}' dengan SKU '{sku}' berhasil ditambahkan!")
      print(inventory[sku])
   except ValueError:
      print("\nError: Stok dan Harga harus berupa angka. Data tidak tersimpan.")

def lihat_inventory(inventory):
   print("\n --- Daftar Inventory ---")
   if not inventory:
      print("Maaf Data di Inventory Masih Kosong")
      return
   else:
      # print(inventory)
      for i, (sku, detail) in enumerate(inventory.items(), 1):
        print(f"{i}. SKU: {sku}")
        print(f"   Nama: {detail['nama']}")
        print(f"   Stok: {detail['stok']}")
        print(f"   Harga: Rp {detail['harga']:,.2f}")
        print(f"   Kategori: {detail['kategori']}")
        print("-" * 25)

def jual_barang(inventory, riwayat):
   try:
      keranjang = input("Masukkan kode SKU :")
      jumlah_jual = int(input("Masukan Jumlah barang :"))

      if keranjang in inventory:
         if inventory[keranjang]['stok'] >= jumlah_jual:
            print(f"Barang dengan SKU :{keranjang} tersedia dan Stok Masih tersedia")
            inventory[keranjang]['stok'] -=jumlah_jual
            riwayat.append({"tipe":"jual","sku":keranjang,"jumlah":jumlah_jual})

            print(f"Berhasil menjual {jumlah_jual} unit '{inventory[keranjang]['nama']}'.")
            print(f"Sisa stok: {inventory[keranjang]['stok']}")
         else:
            print(f"Barang dengan SKU :{keranjang} tersedia dan Stok :{inventory[keranjang]['stok']} tidak mencukupi")
      else:
         print(f"Barang dengan SKU :{keranjang} tidak ada")
   except ValueError:
      print("data yang anda inputkan salah")

def hapus_barang(inventory):
   print("\n --- Hapus Data Barang ---")
   if not inventory:
      print("Data barang Masih Kosong")
      return
   
   try:
      cari_barang = input("Masukan kode SKU : ")

      if cari_barang in inventory:
         inventory.pop(cari_barang)
         print(f"Data Barang {cari_barang} Berhasil di hapus")
   except ValueError:
      print("Data BArang yang di masukkan tidak ada")

def update_barang(inventory,kategori):
   print("\n --- Update Data Barang ---")
   try:
      cari_barang = input("Masukkan Kode barang yang ingin di update :")
      
      if cari_barang in inventory:
         print(f"Data barang Kode SKU :{cari_barang} ditemukan")
         print(f"Data saat ini: {inventory[cari_barang]}")

         print("\n Apa yang ingin diupdate?")
         print("1. ubah SKU")
         print("2. ubah nama dan Kategori")
         print("3. ubah stok barang")
         print("4. ubah harga barang")
         print("5. ubah semuanya")
         pilihan_update = int(input("Masukan Pilihan anda : "))

         if pilihan_update == 1:
            sku_baru = input("Masukkan SKU baru : ")
            # Langsung update SKU tanpa menghapus
            if sku_baru != cari_barang:  # hanya update jika SKU berubah
               inventory[sku_baru] = inventory[cari_barang]  # salin data ke SKU baru
               del inventory[cari_barang]  # hapus entry lama
            print("SKU berhasil di perbaharui")
         elif pilihan_update == 2:
            nama_baru = input("MAsukkan nama baru : ")
            kategori_baru = input("masukkan kategori baru : ")
            inventory[cari_barang]['nama'] = nama_baru
            inventory[cari_barang]['kategori'] = kategori_baru
            kategori.add(kategori_baru)
            print("Nama dan Kategori berhasil di perbaharui")
         elif pilihan_update == 3:
            stok_baru = int(input("Masukkan Stok Baru : "))
            inventory[cari_barang]['stok'] = stok_baru
            print("berhasil update stok")
         elif pilihan_update == 4:
            harga_baru = float(input("Masukkan harga Baru : "))
            inventory[cari_barang]['harga'] = harga_baru
            print("berhasil update harga")
         elif pilihan_update == 5:
            sku_update = input("Masukkan SKU baru : ")
            nama_update = input("MAsukkan nama baru : ")
            stok_update = int(input("Masukkan Stok Baru : "))
            harga_update = int(input("Masukkan harga Baru : "))
            kategori_update = input("masukkan kategori baru : ")

            # Update semua field sekaligus
            if sku_update != cari_barang:  # jika SKU berubah
               inventory[sku_update] = {
                  "nama": nama_update,
                  "stok": stok_update,
                  "harga": harga_update,
                  "kategori": kategori_update
               }
               del inventory[cari_barang]  # hapus entry lama
            else:  # jika SKU tidak berubah
               inventory[cari_barang]['nama'] = nama_update
               inventory[cari_barang]['stok'] = stok_update
               inventory[cari_barang]['harga'] = harga_update
               inventory[cari_barang]['kategori'] = kategori_update
            kategori.add(kategori_update)
            print("Semua data berhasil diupdate!")
         else:
            print("pilihan yang anda masukkan salah")
      else:
         print(f"Barang dengan SKU {cari_barang} tidak ditemukan")
   except ValueError:
      print("Data Yang anda input salah")


# ... lalu panggil fungsi ini dari menu utama Anda  
def main():
   inventory = {}
   kategori = set()
   riwayat = []

   while True:
      print("--- Pilihan Menu Inventory ---")
      print("1. tambah data barang")
      print("2. lihat daftar barang")
      print("3. Jual Barang")
      print("4. hapus Barang")
      print("5. update Barang")
      print("6. keluar")

      try:
         perintah = int(input("Masukkan pilihan menu anda : "))

         if perintah == 1:
            tambah_barang(inventory, kategori)
         elif perintah == 2:
            lihat_inventory(inventory)
         elif perintah == 3:
            jual_barang(inventory, riwayat)
         elif perintah == 4:
            hapus_barang(inventory)
         elif perintah == 5:
            update_barang(inventory, kategori)
         elif perintah == 6:
            print("terimakasih sampai jumpa")
            break
         else:
            print("Pilihan tidak valid. Silakan pilih 1-6.")
      except ValueError:
         input("input yang anda masukkan salah")

main()
