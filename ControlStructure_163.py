# memberikan nilai evaluasi kepada siswa
# menggunakan if,elif
nilaiSiswa = int(input("evaluasi nilai siswa"))
if nilaiSiswa >=90:
    print ("Excellent performance")
elif nilaiSiswa >=80:
    print ("Very Good performance")
elif nilaiSiswa >=70:
    print ("Good performance")
elif nilaiSiswa >60:
    print ("Average performance")

#Membuat fungsi angka_terbesar dan memberi parameternya
def angka_terbesar (a, b, c):
# logika percabangan if,elif,else
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
#memasukkan 3 angka pada variabel dan memanggil fungsi angka_terbesara
#untuk menunjukkan nilai terbesar
no1 = int(input("masukkan no1 "))
no2 = int(input("masukkan no2 "))
no3 = int(input("masukkan no3 "))
print ("nilai terbesar adalah", angka_terbesar(no1,no2,no3))

#Mengambil input dari pengguna
n = int(input("Masukkan panjang deret fibonacci "))
# inisisalisasi daftar fibonacci 2 nlai awal
listNew = [0,1]
#logika kondisional if, elif, else dan menampilkan hasil
#listNew mengambil elemen terakhir
if int(n) == 1 :
    print(listNew[0])
elif int(n) == 2 :
    print(listNew[0:])
else :
    for i in range(int(n)) :
        c = listNew[-1] + listNew[-2]
# append menambahkan hasil penjumlahan tersebut kedalam list
        listNew.append(c)
print(listNew[0:int(n)])

#fungsi yang digunakan untuk mencari dan mencetak angka ganjil
def angka_ganjil():
#input pengguna
    n = int(input("Masukkan batas n untuk angka ganjil: "))
#list untuk angka ganjil
    ganjil = [i for i in range(1, n + 1) if i % 2 != 0]
#mencetak hasil
    print("Angka ganjil hingga", n, "adalah:", ganjil)
# Memanggil fungsi
angka_ganjil()

#membuat fungsi segetika angka
def segitiga_angka():
#input anggota
    n = int(input("Masukkan nilai n untuk segitiga angka: "))
#perulangan untuk membuat segetika, diberi range 
    for i in range(1, n + 1):
#mencetak 
        print((str(i) + ' ') * i)
# Memanggil fungsi
segitiga_angka()