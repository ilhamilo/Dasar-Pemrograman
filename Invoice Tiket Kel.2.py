daftar_film = {
    "Action": {1: "Spider-Man No Way Home", 2: "Rampage", 3: "Fast X"},
    "Horror": {1: "KKN Di Desa Penari", 2: "Pengabdi Setan", 3: "Mata Batin 2"},
    "Comedy": {1: "Agak Laen", 2: "Yowis Ben", 3: "My Stupid Boss"}
}

waktu = {
    "1": "10:00 WIT - 13:30 WIT",
    "2": "14:00 WIT - 19:00 WIT",
    "3": "19:30 WIT - 21:00 WIT"
}

import datetime

def garis():
    print("================================")

while True:
    print("\nWelcome In XXI Jatiland Ternate")
    garis()
    print("1. Beli Tiket")
    print("2. Batal")
    pilihan = input("Pilih nomor yang diinginkan (1/2): ")
    if pilihan == "1":
        while True:
            garis()
            print("Genre yang tersedia : ")
            for genre, value in daftar_film.items():
                print(f"{genre} ")
            garis()
            pilihan = input("Pilih Genre Film : ")
            garis()
            if pilihan in daftar_film:
                print(f"Daftar Film {pilihan} : ")
                for key, value in daftar_film[pilihan].items():
                    print(f"{key}. {value}")
            else:
                print("Genre tidak valid")
                continue
            garis()
            film = input(f"Film yang ingin di tonton (1/2/3): ")
            if film != value and film in value:
                continue
            garis()
            while True:
                print("Jam Tayang :")
                for angka, jam in waktu.items():
                    print(f"{angka}. {jam}")
                garis()
                jam_mulai = input(f"Pilih Jam Tayang (1/2/3): ")
                if jam_mulai in waktu:
                    break
                else:
                    print("Maaf pilihan anda tidak sesuai")
            while True:
                hari = input("Masukkan hari (Senin/Selasa/Rabu/Kamis/Jumat/Sabtu/Minggu): ")
                if hari in ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']:
                    harga = 35000
                elif hari == "Sabtu":
                    harga = 45000
                elif hari == "Minggu":
                    harga = 50000
                else:
                    print("Hari tidak valid. Silakan masukkan nama hari yang benar.")
                    continue
                print("Harga tiket pada", hari, ":", f"Rp {harga:,}")
                break
            garis()
            quantity = int(input("Masukkan jumlah Quantity: "))
            print("Quantity yang diinginkan:", quantity, "orang")
            garis()
            tipe_kursi = input("Pilih tempat duduk (VIP / Reguler): ")
            if tipe_kursi == 'VIP':
                nomor_kursi = [input(f"Masukkan nomor bangku VIP ke-{i+1}: ") for i in range(quantity)]
                biaya_tambahan = 100000 
            elif tipe_kursi == 'Reguler':
                nomor_kursi = [input(f"Masukkan nomor bangku Reguler ke-{i+1}: ") for i in range(quantity)]
                biaya_tambahan = 0
            
            else:
                print("Tempat duduk tidak valid.")
                exit()
            harga = harga * quantity
            total_harga = (harga + biaya_tambahan)

            nama_pembeli = str(input("Masukkan Nama Anda :"))
            umur_pembeli = int(input("Masukan umur anda :"))
            if umur_pembeli >= 17 :
                garis()
                print("Invoice Tiket")
                garis()
                print("Nama:", nama_pembeli)
                print("Usia:", umur_pembeli, "Tahun")
                print("Genre:", pilihan)
                print("Film:", daftar_film[pilihan][int(film)])
                print("Hari:", hari)
                print("Waktu:", waktu[jam_mulai])
                print("Tempat Duduk:", tipe_kursi)
                print("Nomor Bangku:", ", ".join(nomor_kursi))
                print("Quantity:", quantity, "orang")
                print("Harga:", f"Rp {total_harga:,}")
                garis()
            
                konfirmasi = input("Apakah Anda yakin ingin melakukan pembelian? (ya/tidak): ")
                if konfirmasi.lower() == 'ya':
                    lanjutkan_pemesanan = False
                    metode_pembayaran = input("Masukkan metode pembayaran cash/debit : ")
                    print("Anda memilih menggunakan metode pembayaran: ", metode_pembayaran)
                    garis()
                    print("Pembelian berhasil!")
                else:
                    print("Pembelian dibatalkan.")
                break
            else :
                print ("Maaf, Anda tidak dapat membeli tiket")
                exit()
    else:
        print("Pembelian dibatalkan")
    exit()