nama = "Dimas Setiawan" #seharusnya ditambah tanda kutip ("")
umur = 21 #seharusnya hilangkan tanda kutip ("")
berat = 65.4 #seharusnya hilangkan tanda kutip ("")
tinggi = 170 
bmi = berat/((tinggi/100)**2) 
status_siswa = True #seharusnya hilangkan tanda kutip ("")

print(" Nama : ", nama)
print(" Umur : ", umur +1, " tahun")
print(" Berat Badan : ", berat, " kg")
print(" BMI : ", round(bmi, 2))
print(" Siswa Aktif : ", bool (status_siswa))