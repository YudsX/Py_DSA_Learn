from array import *
arr = array('i', [10, 20, 30, 40, 50])

# Menampilkan semua array yang ada dalam list
# Program Utama
if __name__=='__main__':
    for i in arr:
        print(i)

quit() 

# Mengakses data berdasarkan index nya lalu mencetak
if __name__=='__main__':
    print(arr[0])
    print(arr[2])
quit()

# Menggunakan Insert
if __name__=='__main__':
    arr.insert(1, 65) # <- Sisipkan di index array ke 1
    arr.append(int(input(f"Masukan angka random: "))) # <- Menambah angka baru di akhir list
    for i in arr:
        print(i)
quit()

arr = array('q', [])

def isiArray(inputan: int): 
    j = 1
    while j <= inputan:
        baca = int(input(f'Angka ke[{j}] = '))
        arr.insert(j, baca)
        j += 1
    print()

    print("Hasil Insert Angka")
    print("-"*40)
    print(arr)

if __name__=='__main__':
    inputan = int(input("Masukan Banyaknya Angka: "))
    isiArray(inputan) 

