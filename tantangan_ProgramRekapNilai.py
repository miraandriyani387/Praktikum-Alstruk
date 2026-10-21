# ==========================================
# TANTANGAN TERINTEGRASI – Program Rekap Nilai
# ==========================================

print("=== REKAP NILAI MAHASISWA 1 ===")
# 1. Simpan nama mahasiswa
nama_1 = "Aurelia Kalea"

# 2. Simpan nilai tugas dan ujian (Kombinasi 1: Lulus)
nilai_tugas_1 = 82.5
nilai_ujian_1 = 88.0

# 3. Hitung rata-rata
rata_rata_1 = (nilai_tugas_1 + nilai_ujian_1) / 2

# 4. Memeriksa status kelulusan (minimal 75)
status_lulus_1 = rata_rata_1 >= 75

# 5. Tampilkan hasil rekap
print("Nama Mahasiswa :", nama_1)
print("Nilai Tugas    :", nilai_tugas_1)
print("Nilai Ujian    :", nilai_ujian_1)
print("Rata-rata      :", rata_rata_1)
print("Status Lulus   :", status_lulus_1)

print("\n" + "="*40 + "\n")

print("=== REKAP NILAI MAHASISWA 2 ===")
# Kombinasi 2: Tidak Lulus
nama_2 = "Julian Arlo"
nilai_tugas_2 = 68.0
nilai_ujian_2 = 72.0

rata_rata_2 = (nilai_tugas_2 + nilai_ujian_2) / 2
status_lulus_2 = rata_rata_2 >= 75

print("Nama Mahasiswa :", nama_2)
print("Nilai Tugas    :", nilai_tugas_2)
print("Nilai Ujian    :", nilai_ujian_2)
print("Rata-rata      :", rata_rata_2)
print("Status Lulus   :", status_lulus_2)