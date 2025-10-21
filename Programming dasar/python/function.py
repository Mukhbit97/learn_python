
# function
def sapa():
   print("Hallo selamat datang di python!")

# memanggil function
sapa()

# function dengan parameter
def sapa_nama(nama):
   print(f"halo {nama}, semoga harimu menyenangkan")

sapa_nama("budi")
sapa_nama("siti")

# function dengan return value
def tambah(a, b):
   return a + b

hasil = tambah(5, 7)
print(f"hasil penjumlahan : {hasil}")

#  default parameter
def sapa_orang(nama="teman"):
   print(f"hallo {nama}")

sapa_orang("andi")
sapa_orang()

# function dengan banyak argument (non-keyword argument dan keyword argument)
# args
def jumlahkan(*angka):
   total = sum(angka)
   print("total :", total)

jumlahkan(1,2,3,4,5) #bisa input banyak angka

# kwargs
def biodata(**data):
   for key, value in data.items():
      print(f"{key} : {value}")

biodata(nama="budi", umur=20, kota="jakarta")
