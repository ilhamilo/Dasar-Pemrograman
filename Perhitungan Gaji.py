Nama = input("Masukkan Nama Anda : ")
hari_kerja = int(input("Hari Selama Dia Bekerja : "))
hari_lembur = int (input("Hari Dia Lembur : "))

hari_kerja_perbulan = 26
gaji_bersih = 3800000
gaji_lembur_perhari = 200000

gaji_lembur = gaji_lembur_perhari * hari_lembur 

gaji_total = int((hari_kerja/hari_kerja_perbulan)*gaji_bersih + gaji_lembur)
gaji_total = f"{gaji_total:,}".replace(",",".")

print("Gaji Yang didapatkan sebesar : Rp.", gaji_total)