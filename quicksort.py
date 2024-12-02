import time
def partition (a, start, end):  
    i = start - 1
    pivot = a[end] # pivot element  
      
    for j in range(start, end):  
        # If current element is smaller than or equal to the pivot  
        if (a[j] < pivot):
            i = i + 1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

            """
            a[i], a[j] = a[j], a[i]
            """ 
            print(f"               {start} {end}")
      
    a[i+1], a[end] = a[end], a[i+1]  
    return (i + 1)  
      
# function to implement quick sort   
def quick(a, start, end): # a[] = array to be sorted, start = Starting index, end = Ending index   
    print(a)
    if (start < end):  
        p = partition(a, start, end) # p is partitioning index 
        print(p)
        time.sleep(1)
        quick(a, start, p - 1)  
        quick(a, p + 1, end)  
  
          
def printArr(a): # function to print the array  
    for i in range(len(a)):  
        print (a[i], end = " ")  
  
      
a = [1, 2, 3, 4, 5, 6]  
print("Before sorting array elements are - ")  
printArr(a)
print("")
quick(a, 0, len(a)-1)
print("\nAfter sorting array elements are - ")  
printArr(a)  


"""
Mari kita jelaskan output kode tersebut berdasarkan urutan pemanggilan fungsi dan apa yang terjadi dalam setiap iterasi.

Pertama, kita memanggil fungsi quick(a, 0, len(a)-1) dengan array a yang belum diurutkan dan indeks awal dan akhir
dari array tersebut.

Fungsi quick pertama kali dipanggil dengan start = 0 dan end = 5 (indeks awal dan akhir dari array).

Di dalam fungsi quick, kondisi start < end terpenuhi, maka kita lanjut ke pemanggilan fungsi partition.

Fungsi partition dipanggil dengan start = 0 dan end = 5. Pivot dipilih sebagai elemen terakhir dari array, yaitu 7.

Proses partisi dimulai. Kita perbandingkan setiap elemen array dengan pivot dan pindahkan elemen-elemen yang lebih
kecil ke sebelah kiri pivot dan elemen-elemen yang lebih besar ke sebelah kanan pivot.

Proses partisi dilakukan dalam loop for j in range(start, end). Saat ini, loop akan berjalan dari indeks 0 hingga 4.

Iterasi 1: Bandingkan 9 (a[0]) dengan pivot (7), tidak memenuhi kondisi, lanjutkan.
Iterasi 2: Bandingkan 8 (a[1]) dengan pivot (7), tidak memenuhi kondisi, lanjutkan.
Iterasi 3: Bandingkan 4 (a[2]) dengan pivot (7), memenuhi kondisi, tukar dengan elemen ke-1 (a[i+1]).
Output: 4 9
Iterasi 4: Bandingkan 6 (a[3]) dengan pivot (7), memenuhi kondisi, tukar dengan elemen ke-2 (a[i+1]).
Output: 6 8
Iterasi 5: Bandingkan 5 (a[4]) dengan pivot (7), memenuhi kondisi, tukar dengan elemen ke-3 (a[i+1]).
Output: 5 7
Setelah loop selesai, kita memiliki array yang terpartisi menjadi [4, 6, 5, 7, 9, 8], dengan pivot (7) di posisi ke-3.

Kita pindahkan pivot ke posisi yang benar di antara elemen yang lebih kecil dan lebih besar dari pivot.

Pivot dipindahkan ke posisi ke-4, setelah elemen 5.
Output: 7 9
Fungsi partition mengembalikan indeks pivot yang sekarang adalah 4.

Kita panggil rekursi untuk bagian array sebelum dan sesudah pivot.

Pertama, rekursi dipanggil untuk bagian sebelum pivot dengan start = 0 dan end = 3.
Kedua, rekursi dipanggil untuk bagian setelah pivot dengan start = 5 dan end = 5.
Proses ini terus berlanjut hingga seluruh array terurut.

Setelah rekursi selesai, kita mencetak array yang sudah diurutkan.

Dengan demikian, output tersebut mencerminkan proses partisi dan pengurutan cepat (quicksort) yang dilakukan oleh program."""