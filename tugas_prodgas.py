def garis():
    print("----------")

#fungsi bubble sort ascending (dari kecil ke besar)
def sort_asc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range (n-i-1):
            #membandingkan masing" elemen ke kanan
            if array [j] > array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
    return array

#fungsi bubble sort descending (dari besar ke kecil)
def sort_desc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range (n-i-1):
            #membandingkan masing" elemen ke kanan
            if array [j] < array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
    return array

#fungsi rata rata
def rata_rata(angka):
    return sum(angka)/len(angka)

#input nilai
garis()
print("masukkan tiga buah nilai")
nama = (input("masukan nama anda : "))
nilai_a = int(input("nilai 1 : "))
nilai_b = int(input("nilai 2 : "))
nilai_c = int(input("nilai 3 : "))
nilai_d = int(input("nilai 4 : "))
nilai_e = int(input("nilai 5 : "))
nilai_f = int(input("nilai 6 : "))
nilai_g = int(input("nilai 7 : "))
nilai_h = int(input("nilai 8 : "))
nilai_i = int(input("nilai 9 : "))
nilai_j = int(input("nilai 10 : "))
angka = [nilai_a, nilai_b, nilai_c, nilai_d, nilai_e, nilai_f, nilai_g, nilai_h, nilai_i, nilai_j]
garis()
print()

#nilai akhir
print("hasil akhir----")
#nama
print("nama anda : ",(nama))
print("urutan angka ascending : ", (sort_asc(angka)))
print("urutan angka descending : ", (sort_desc(angka)))
garis()
print()

#angka terbesar
print("angka terbesar : ",max(angka))

#angka terkecil
print("angka terkecil : ",min(angka))

#rata rata
print("rata rata : ",round(rata_rata(angka),2))

#jumlah angka
print("jumlah angka : ",sum(angka))
