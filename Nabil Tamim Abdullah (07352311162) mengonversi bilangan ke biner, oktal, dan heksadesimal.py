bilangan = int(input("Masukkan Bilangan: "))

#mengonversi ke bilangan biner
bilangan_biner = bin (bilangan)[2:]
bilangan_biner = bilangan_biner.zfill(8)
print("Hasil Konversi Ke Bilangan Biner: ",[bilangan_biner])

#mengonversi ke bilangan oktal
print("Hasil Konversi Ke Bilangan Oktal: ", oct(bilangan)[2:])

#mengonversi ke bilangan heksadesimal
print("Hasil Konversi Ke Heksadesimal : ", hex(bilangan)[2:].upper())