x = int (input ("Enter an number :")) 

bilangan_biner = bin (x)[2:]
bilangan_biner = bilangan_biner.zfill(8)

print ("Hasil Konversi Ke Biner: ",[bilangan_biner])
print("Hasil Konversi Ke Oktal: ", oct(x)[2:])
print("Hasil Konversi Ke Heksadesimal : ", hex(x)[2:].upper())