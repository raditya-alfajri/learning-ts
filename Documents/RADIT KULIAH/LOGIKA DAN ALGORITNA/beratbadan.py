weights = []
n = int(input("Masukkan jumlah minggu pemantauan: "))

if n <= 0:
    print("Jumlah minggu tidak boleh 0 atau negatif!")
else:
    for i in range(n):
        print("Minggu ke-", i+1)
        weight = float(input("Masukkan berat badan (kg): "))
        weights.append(weight)

    firstWeight = weights[0]
    lastWeight = weights[-1]
    diff = firstWeight - lastWeight
    
    print("berat awal: ", firstWeight, "kg")
    print("berat akhir: ", lastWeight, "kg")
    print("total perubahan: ", diff, "kg")

    
    if diff >= 2:
        print("Progress bagus!")
    elif diff < 2 and diff >= 0:
        print("Pertahankan pola makanmu.")
    else:
        print("Perlu evaluasi kembali pola makan.")