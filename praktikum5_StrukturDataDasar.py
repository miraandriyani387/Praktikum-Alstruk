# Data awal
nilai = [78, 85, 90, 85]
mahasiswa = {"nama": "Nadia", "kelas": "IF-A"}
koordinat = (5, 8)
angka = {2, 4, 4, 6, 8}

# Task 1: Tampilkan nilai pertama dari list
print("1. Nilai pertama dari list        :", nilai[0])

# Task 2: Tambahkan nilai 95 ke list dan tampilkan list terbaru
nilai.append(95)
print("2. List terbaru setelah append(95):", nilai)

# Task 3: Tampilkan nama mahasiswa dari dictionary
print("3. Nama mahasiswa dari dictionary :", mahasiswa["nama"])

# Task 4: Tampilkan koordinat pertama dari tuple
print("4. Koordinat pertama dari tuple   :", koordinat[0])

# Task 5: Tampilkan angka unik dengan sorted(angka)
print("5. Angka unik (sorted)            :", sorted(angka))

# Task 6: Penjelasan mengenai Set
print("\n=== PENJELASAN TENTANG SET ===")
print("Set bersifat unik dan otomatis menghapus elemen duplikat.")