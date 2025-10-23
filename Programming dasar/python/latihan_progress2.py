
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
      print(inventory)
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

   # output masuh belum sesuai dengan yang di harapkan nanti di perbaiki

# ... lalu panggil fungsi ini dari menu utama Anda  
def main():
   inventory = {}
   kategori = set()

   while True:
      print("--- Pilihan Menu Inventory ---")
      print("1. tambah data barang")
      print("2. lihat daftar barang")
      # print("3. cari kontak")
      # print("4. hapus kontak")
      # print("5. update kontak")
      print("6. keluar")

      try:
         perintah = int(input("Masukkan pilihan menu anda : "))

         if perintah == 1:
            tambah_barang(inventory, kategori)
         elif perintah == 2:
            lihat_inventory(inventory, kategori)
         else:
            print("terimakasih sampai jumpa")
            break
      except ValueError:
         input("input yang anda masukkan salah")

main()
