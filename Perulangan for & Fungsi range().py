# 1. Perulangan for dasar (iterasi langsung pada list)
print("Contoh 1: Perulangan pada list")
makanan = ["nasi goreng", "mie ayam", "sate"]
for item in makanan:
    print("Saya suka", item)

# Output:
# Saya suka nasi goreng
# Saya suka mie ayam
# Saya suka sate

# 2. Perulangan menggunakan range(angka)
print("Contoh 2: Perulangan menggunakan range()")
for i in range(5):
    print("Urutan:", i)

# Output:
# Urutan: 0
# Urutan: 1
# Urutan: 2
# Urutan: 3
# Urutan: 4

# 3. range(mulai, akhir)
print("Contoh 3: range(mulai, akhir)")
for i in range(1, 6):
    print("Angka:", i)

# Output:
# Angka: 1
# Angka: 2
# Angka: 3
# Angka: 4
# Angka: 5

# 4. range(mulai, akhir, langkah)
print("Contoh 4: range dengan langkah (step)")
for i in range(0, 10, 2):
    print("Kelipatan 2:", i)

# Output:
# Kelipatan 2: 0
# Kelipatan 2: 2
# Kelipatan 2: 4
# Kelipatan 2: 6
# Kelipatan 2: 8