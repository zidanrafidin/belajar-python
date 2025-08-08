# Perulangan break & continue.py
# Perulangan break & continue digunakan untuk mengontrol alur perulangan.

# "break" : Berhenti dan keluar dari perulangan.

# contoh perulangan break :
while True:
    n = int(input("masukkan nomer habis bagi 2: "))
    if n % 2 != 0:
        break

    print("%d habis dibagi 2" % (n))


# "continue" : Melewati sisa kode di perulangan saat ini dan langsung lanjut ke perulangan berikutnya.

# contoh perulangan continue
for i in range(10):
    if i < 5 or i > 9:
        continue
    print("number", i)
print("selesai")
# output :
# number 5
# number 6
# number 7
# number 8
# number 9
