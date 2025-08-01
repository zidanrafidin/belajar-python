# Iterasi Elemen Data Kolektif

# 1. Perulangan `for` dasar (iterasi langsung pada list)
# Kita bisa langsung pake `for` buat ngulang item di dalam **list**.
# Python bakal ngunjungin tiap item satu per satu, sesuai urutannya.

print("Contoh 1: Perulangan pada list")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Saya suka", fruit)

# Output:
# Saya suka apple
# Saya suka banana
# Saya suka cherry

# ---

# 2. Iterasi langsung pada tuple
# Mirip kayak list, kalo kamu ngiterasi **tuple**, Python bakal ngambil tiap elemennya sesuai urutan juga.

print("Contoh 2: Perulangan pada tuple")
coordinates = (10, 20)
for coord in coordinates:
    print("Koordinat:", coord)

# Output:
# Koordinat: 10
# Koordinat: 20

# ---

# 3. Iterasi langsung pada string
# Nah, kalo kamu pake `for` buat **string**, Python bakal ngambil tiap karakter yang ada di string itu, satu per satu.

print("Contoh 3: Perulangan pada string")
for char in "Python":
    print("Karakter:", char)

# Output:
# Karakter: P
# Karakter: y
# Karakter: t
# Karakter: h
# Karakter: o
# Karakter: n

# ---

# 4. Iterasi langsung pada dictionary (mengambil key)

print("Contoh 4: Perulangan pada dictionary (key)")
student_grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C"
}
for name in student_grades:
    print(f"Nilai {name}: {student_grades[name]}")

# Output:
# Nilai Alice: A
# Nilai Bob: B
# Nilai Charlie: C

# ---

# 5. Iterasi langsung pada set
# **Set** itu koleksi item yang nggak punya urutan dan nggak boleh ada yang dobel.

print("\nContoh 5: Perulangan pada set")
unique_numbers = {1, 5, 2, 5, 3}
for num in unique_numbers:
    print("Angka unik:", num)

# Output (urutan bisa beda-beda ya):
# Angka unik: 1
# Angka unik: 2
# Angka unik: 3
# Angka unik: 5
