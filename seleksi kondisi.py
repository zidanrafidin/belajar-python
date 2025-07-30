"""
Ringkasan materi kondisi yang saya dapat setelah belajar:
Pernyataan kondisional 'if', 'elif', 'else' dalam Python

- 'if': Jalankan kode JIKA kondisi True.
- 'elif': Jalankan kode JIKA 'if' sebelumnya False DAN kondisi 'elif' ini True.
- 'else': Jalankan kode JIKA SEMUA kondisi di atasnya False.
"""

# --- Contoh Penggunaan ---

nilai = 75

if nilai >= 90:
    print("Nilai Anda: A")
elif nilai >= 80:
    print("Nilai Anda: B")
elif nilai >= 70:
    print("Nilai Anda: C")
else:
    print("Nilai Anda: D atau E")

# Output untuk nilai = 75 adalah: Nilai Anda: C