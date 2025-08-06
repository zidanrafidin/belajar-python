# PERULANGAN WHILE 
# Perulangan while terus berjalan selama kondisi logika atau nilai yang ditetapkan masih 
# terpenuhi (bernilai true).

# Contoh penggunaan perulangan while untuk meminta input dari pengguna 
# dan memeriksa apakah input tersebut adalah bilangan genap yang lebih besar dari 0.

should_continue = True

while should_continue:
    n = int(input("masukkan angka genap lebih besar dari 0: "))

    if n <= 0 or n % 2 == 1:
        print(n, "bukan bilangan genap yang lebih besar dari 0")
        should_continue = False
    else:
        print("number:", n)


# Contoh penggunaan perulangan while untuk mencetak angka dari 0 hingga n-1.

n = int(input("enter max data: "))
i = 0

while i < n:
    print("number", i)
    i += 1

# while dan for sekilas memang terlihat sama namun yang menjadi pembeda adalah :
# Loop "for" digunakan saat sudah tahu pasti berapa kali pengulangan itu akan terjadi.
# Loop "while" digunakan saat kamu tidak tahu pasti berapa kali pengulangan akan terjadi.
