print("selamat datang di warung kopi ceria!")
print("daftar Harga")
print("kopi : 15.000/gelas")
print("sandwich : 25.000/porsi")
print("kentang : 20.000/porsi")

print("rincian pembelian :")
kopi = int(input("kopi :"))
sandwich = int(input("sandwich :"))
kentang = int(input("kenttang :"))

harga_kopi = 15000
harga_sandwich = 25000
harga_kentang = 20000

total_harga = (harga_kopi * kopi) + (harga_sandwich * sandwich) + (harga_kentang * kentang)
print(f"total harga : {total_harga} ")
bayar = int(input("uang yang dibayarkan : "))
cukup = bayar >= total_harga
print(f"apakah uangmu cukup? {cukup}")
kembalian = bayar - total_harga
print(f"kembalianmu : {kembalian}")