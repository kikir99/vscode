# Minta input nilai dari pengguna
matematika = float(input("Masukkan nilai Matematika (0-100): "))
bahasa_indonesia = float(input("Masukkan nilai Bahasa Indonesia (0-100): "))
ipa = float(input("Masukkan nilai IPA (0-100): "))

# Hitung rata-rata nilai
rata_rata = (matematika + bahasa_indonesia + ipa) / 3

# Tentukan status kelulusan
if matematika > 85 and bahasa_indonesia > 85 and ipa > 85:
    status = "Lulus dengan Predikat Istimewa"
elif matematika < 70 and (bahasa_indonesia > 80 and ipa > 80):
    status = "Lulus Bersyarat"
elif bahasa_indonesia < 70 and (matematika > 80 and ipa > 80):
    status = "Lulus Bersyarat"
elif ipa < 70 and (matematika > 80 and bahasa_indonesia > 80):
    status = "Lulus Bersyarat"
elif matematika < 70 or bahasa_indonesia < 70 or ipa < 70:
    # Jika satu atau lebih nilai di bawah 70
    if (matematika < 70) + (bahasa_indonesia < 70) + (ipa < 70) >= 2:
        status = "Tidak Lulus"
    else:
        status = "Lulus Bersyarat"
elif rata_rata < 75:
    status = "Tidak Lulus"
else:
    status = "Lulus"

# Cetak status akhir siswa
print("Status kelulusan siswa:", status)
