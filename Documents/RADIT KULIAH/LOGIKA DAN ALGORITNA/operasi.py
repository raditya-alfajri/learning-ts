print("Selamat datang di game store!")
print("harga 1 diamond adalah : 2000")
diamond = int(input("jumlah diamond yang dibeli : "))

harga_diamond = 2000
total = harga_diamond * diamond

print(f"total bayar : {total} ")
bayar = int(input("uang yang dibayarkan : "))
cukup = bayar >= harga_diamond
print(f"apakah uangmu cukup? {cukup}")

kembalian = bayar - total
print(f"kembalianmu : {kembalian}")
