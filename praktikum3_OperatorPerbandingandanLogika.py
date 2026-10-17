# Task 1: Membuat variabel nilai dan kehadiran
nilai = 82
kehadiran = 90

# Task 2: Menggunakan operator >= untuk memeriksa masing-masing syarat
syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

print("=== PENGECEKAN DATA AWAL ===")
print("Nilai >= 75     :", syarat_nilai)
print("Kehadiran >= 80%:", syarat_kehadiran)

# Task 3: Menggunakan operator and untuk menentukan kelulusan
memenuhi_semua = syarat_nilai and syarat_kehadiran
print("Lulus (menggunakan AND):", memenuhi_semua)

# Task 4: Mengubah nilai menjadi 70 dan mengamati hasil
nilai = 70
syarat_nilai_baru = nilai >= 75
memenuhi_semua_baru = syarat_nilai_baru and syarat_kehadiran

print("\n=== SETELAH NILAI DIUBAH MENJADI 70 ===")
print("Nilai >= 75     :", syarat_nilai_baru)
print("Kehadiran >= 80%:", syarat_kehadiran)
print("Lulus (menggunakan AND):", memenuhi_semua_baru)

# Task 5: Menggunakan operator or
lulus_or = syarat_nilai_baru or syarat_kehadiran
print("\n=== MENGGUNAKAN OPERATOR OR (Nilai = 70) ===")
print("Lulus (menggunakan OR) :", lulus_or)