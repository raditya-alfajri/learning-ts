mahasiswa = {
    "25090008": {
        "nama": "Muhammad Raditya Alfajri",
        "jurusan": "Teknik Informatika",
        "nilai": {
            "algoritma":100,
            "Matematika":90,
            "python":95,
            
        }
    },
    "25090007": {
        "nama": "Andika Damarjati",
        "jurusan": "Teknik Informatika",
        "nilai": {
            "algoritma":90,
            "Matematika":90,
            "python":100,
            
        }
    },
      "25090034": {
          "nama": "Muhammad Araf Firdaus",
          "jurusan": "Teknik Informatika",
          "nilai": {
              "algoritma":90,
              "Matematika":85,
              "python":90,
              
          }
      },
      "25090035": {
          "nama": "Reyhan Faisal Ahmad",
          "jurusan": "Teknik Informatika",
          "nilai": {
              "algoritma":95,
              "Matematika":85,
              "python":85,
              
          }
      },    
      "25090025": {
          "nama": "Arden Bima Ramadani",
          "jurusan": "Teknik Informatika",
          "nilai": {
              "algoritma":85,
              "Matematika":90,
              "python":90,
              
          }
      },
      "25090029": {
          "nama": "Muhammad Zidna Fadla",
          "jurusan": "Teknik Informatika",
          "nilai": {
              "algoritma":95,
              "Matematika":95,
              "python":100,
              
          }
      },
      "25090014": {
          "nama": "Aliza Rizki Beria",
          "jurusan": "Teknik Informatika",
          "nilai": {
              "algoritma":90,
              "Matematika":100,
              "python":90,
              
          }
      },
      "25090006": {
          "nama": "Iqbal Maulana Syifa",
          "jurusan": "Teknik Informatika",
          "nilai": {
              "algoritma":100,
              "Matematika":90,
              "python":90,
              
          }
      },
      "25090012": {
          "nama": "Putra Tarnandes",
          "jurusan": "Teknik Informatika",
          "nilai": {
              "algoritma":80,
              "Matematika":85,
              "python":85,
              
          }
      },
      "25090032": {
          "nama": "Raihan Putra Khairullah",
          "jurusan": "Teknik Informatika",
          "nilai": {
              "algoritma":90,
              "Matematika":95,
              "python":90,
              
          }
      }
      
}
    
def tampilkan_data():
    print("\nDATA MAHASISWA")
    for nim in mahasiswa:
            print("NIM:", nim)
            print("Nama:", mahasiswa[nim]["nama"])
            print("Jurusan:", mahasiswa[nim]["jurusan"])
            print("Nilai:")
            for data in mahasiswa[nim]["nilai"]:
                print(" ", data, ":", mahasiswa[nim]["nilai"][data])
            print("")

def tambah_data():
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")

        nilai = {
            "algoritma": int(input("Masukkan Nilai Algoritma: ")),
            "matematika": int(input("Masukkan Nilai Matematika: ")),
            "python": int(input("Masukkan Nilai Python: ")),
            }
        
        mahasiswa[nim] = {
            "nama": nama,
            "jurusan": jurusan,
            "nilai": nilai,
        }

        print("Data mahasiswa berhasil ditambahkan")
        
def hapus_data():
        nim = input("Masukkan NIM yang ingin dihapus: ")
        if nim in mahasiswa:
            del mahasiswa[nim]
            print("Data berhasil dihapus")
        else:
            print("Data tidak ditemukan")
        
def update_nilai():
    nim = input("Masukkan NIM: ")
    if nim in mahasiswa:
        data = input("Masukkan mata kuliah yang ingin diubah: ")
        if data in mahasiswa[nim]["nilai"]:
            nilai_baru = int(input("Masukkan nilai baru: "))
            mahasiswa[nim]["nilai"][data] = nilai_baru
            print("Nilai berhasil diupdate")
        else:
            print("Mata kuliah tidak ditemukan")
    else:
        print("NIM tidak ditemukan")

def nilai_python_tertinggi():
    tertinggi = 0
    daftar_nama = []

    for nim in mahasiswa:
        nilai = mahasiswa[nim]["nilai"]["python"]
        nama = mahasiswa[nim]["nama"]

        if nilai > tertinggi:
            tertinggi = nilai
            daftar_nama = [nama]   
            
        elif nilai == tertinggi:
            daftar_nama.append(nama)

    print("Mahasiswa dengan nilai Python tertinggi:", tertinggi)
    for n in daftar_nama:
        print("-", n)


def rata_rata_nilai():
    total = {}
    jumlah = {}

    for nim in mahasiswa:
        for data in mahasiswa[nim]["nilai"]:
            total[data] = total.get(data, 0) + mahasiswa[nim]["nilai"][data]
            jumlah[data] = jumlah.get(data, 0) + 1

    print("Rata-rata nilai tiap mata kuliah:")
    for data in total:
        print(data, ":", total[data] / jumlah[data])
        
def cari_mahasiswa():
    nama_cari = input("Masukkan nama mahasiswa: ")
    ditemukan = False

    for nim in mahasiswa:
        if mahasiswa[nim]["nama"].lower() == nama_cari.lower():
            print("\nData ditemukan")
            print("NIM:", nim)
            print("Nama:", mahasiswa[nim]["nama"])
            print("Jurusan:", mahasiswa[nim]["jurusan"])
            print("Nilai:")
            for data in mahasiswa[nim]["nilai"]:
                print(" ", data, ":", mahasiswa[nim]["nilai"][data])
            ditemukan = True

    if not ditemukan:
        print("Mahasiswa tidak ditemukan")
        
while True:
    print("\nMENU")
    print("1. Tampilkan Data Mahasiswa")
    print("2. Tambah Data Mahasiswa")
    print("3. Hapus Data Mahasiswa")
    print("4. Update Nilai Mata Kuliah")
    print("5. Mahasiswa dengan Nilai Python Tertinggi")
    print("6. Rata-rata Nilai Tiap Mata Kuliah")
    print("7. Cari Mahasiswa")
    print("8. Keluar")

    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        update_nilai()
    elif pilihan == "5":
        nilai_python_tertinggi()
    elif pilihan == "6":
        rata_rata_nilai()
    elif pilihan == "7":
        cari_mahasiswa()
    elif pilihan == "8":
        print("Program Selesai Terima kasih")
        break
    else:
        print("Pilihan tidak valid")