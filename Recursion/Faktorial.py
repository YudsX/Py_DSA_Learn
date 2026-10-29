'''
---------------------------------------------------
 Nama Berkas : Faktorial.py
 Tujuan      : Membuat program Faktorial dengan cara 
               Rekursif dalam bahasa pemrograman Python
 Penterjemah : Thonny Python 3.7.4
 Pemrogram   : Asep Budiman Kusdinar, M.T., M.T.A.
---------------------------------------------------
'''
#-->Buat Fungsi Faktorial secara Rekursif
def fakt(n):
    if 0<=n<=1: return 1
    else: return n * fakt(n-1) 
    return fakt(n)

#-->Buat Fungsi Untuk Isi Data
def isiData():
    try:
        n = int(input("Masukkan banyaknya data = "))
        if 0<=n<=99:
            print(n," Faktorial adalah\n")
            print('%d! = ' % n, end='')
            i=n
            while i>= 1:
                if (i == 1):
                    print("%d = " % i, end='')
                else:
                    print("%d x " % i, end='')
                i-=1
            print(fakt(n))
        else:
            print(' Perintah salah, Untuk sementara angka dibatasi,\n',
                  'antara 0-99 (100 Angka)..!!!')
    except Exception as Error: #-->Cek jika sistem eror
        print()
        print("This error: %s " %Error)
        tanya()

#-->Buat Fungsi Tanya untuk Pengguna
def tanya():
    print()
    kar = input('Coba Lagi (Y/T)? ')
    if kar.upper() == 'Y':
        print()
        isiData()
        tanya()
    elif kar.upper() == 'T':
        print()
        print('Terimakasih sudah mencoba ...')
        quit()
    else:
        print()
        print('Maaf..perintah tidak dikenali..!!')
        tanya()
    return tanya()

#-->Program Utama
if __name__=='__main__':
    print("Faktorial dengan Cara Rekursif")
    print("------------------------------")
    isiData() #-->Panggil Fungsi Isi Data
    tanya() #-->Panggil Fungsi Tanya Pengguna