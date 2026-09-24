hari_konser = input('masukkan hari konser (biasa/akhir_pekan): ')
status_pembeli = input('masukkan status pembeli (member/non member): ')
jumlah_tiket = int(input('masukkan jumalh tiket: '))

if hari_konser == "biasa":
    if status_pembeli == "member":
        harga = 45000 * jumlah_tiket
    elif status_pembeli == "non member":
        harga = 60000 * jumlah_tiket    
        print(f"total harga {harga}")
    else:
        print('input tidak valid')
elif hari_konser == "akhir_pekan":
    if status_pembeli == "member":
        harga = 70000 * jumlah_tiket
    elif status_pembeli == "non member":
        harga = 90000 * jumlah_tiket
        print(f"total harga {harga}")
    else:
        print("input tidak valid")

diskon = 10
harga_diskon = (harga * jumlah_tiket * diskon ) / 100

