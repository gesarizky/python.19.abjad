# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput Huruf
kalimat = input("Tulis Sebuah Huruf: ")

# Memecah Kalimat menjadi Kata-Kata
kata = kalimat.split()

# Mengurutkan Kata-Kata
kata.sort()

# Menampilkan Kata-Kata yang Telah Diurutkan
print("Berikut Urutan Huruf:")
for urut in kata:
   print(urut)
