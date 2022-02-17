print ("SELAMAT DATANG DI TOKO OBAT STUTLE")

def garis():
    print("_____________________________________________")
garis()
def menu ():
    print ("_____________________________________________")
    print ("  ID PRODUK  |     NAMA PRODUK     |  HARGA  ")
    print ("      1      |  ANTISEPTIK         |  Rp.10000 ")
    print ("      2      |  OBAT FLU           |  Rp.5000")
    print ("      3      |  VITAMIN/SUPLEMENT  |  Rp.7500")
    print ("      4      |  TETES MATA         |  Rp.15000")
    print ("      5      |  PARACETAMOL        |  Rp.3000")
    
BukaMenu = input ("Ingin Membuka Menu ? (Y/N):")
if BukaMenu == "y" or BukaMenu == "Y" :
    menu()
else:
    pass

id_produk = []
nama_produk = []
harga = []
jumlah_beli = []
jumlah_harga = []
uang_bayar = []
uang_kembali = []
total_belanja = []

garis()
nama = input ("Masukan Nama Pembeli :")
jumlah_transaksi =  int (input ("Masukan Jumlah Transaksi :"))
garis()
i = 0
while i < jumlah_transaksi :
    print ("Data ke-",i+1)
    id_produk.append(int(input("Masukan ID Produk :")))
    jumlah_beli.append(int(input("Masukan Jumlah Beli :")))
    if id_produk[i]== 1 :
        nama_produk.append("ANTISEPTIK       ")
        harga.append(10000)
        jumlah_harga.append(jumlah_beli[i]*int("10000"))
    elif id_produk[i]== 2 :
        nama_produk.append("OBAT FLU         ")
        harga.append(5000)
        jumlah_harga.append(jumlah_beli[i]*int(5000))
    elif id_produk[i]== 3 :
        nama_produk.append("VITAMIN/SUPLEMENT")
        harga.append(7500)
        jumlah_harga.append(jumlah_beli[i]*int(7500))
    elif id_produk[i]== 4 :
        nama_produk.append("TETES MATA       ")
        harga.append(15000)
        jumlah_harga.append(jumlah_beli[i]*int(15000))
    elif id_produk[i]== 5 :
        nama_produk.append("PARACETAMOL      ")
        harga.append(3000)
        jumlah_harga.append(jumlah_beli[i]*int(3000))
    else :
        nama_produk.append("ID TIDAK ADA     ")
        harga.append("0")
        jumlah_harga.append(jumlah_beli[i]*int(0))
    i+=1

a = 0
total_belanja = 0
print("----------------------------------")
print("DAFTAR BELANJA ANDA")
print("----------------------------------")
print ("Jumlah Barang Yang Anda Beli :" , jumlah_transaksi)
while a < jumlah_transaksi :
    print (a+1, "\t Nama Produk : ", nama_produk[a] , "\t banyak : " , jumlah_beli[a],"\t Harga/1 :Rp", harga[a])
    a+=1

s = 0
hapus = input ("Apakah Anda Ingin Menghapus Pesanan ? (Y/N):")
if hapus == "y" or hapus == "Y" :
    Banyak = int(input("Berapa Banyak Yang Ingin Anda Hapus ? :"))
    f = jumlah_transaksi
    f = f - Banyak
    z = 0 
    while z < Banyak :
        barang = int(input("Silahkan Ketik Urutan Yang Ingin Anda hapus :"))
        del nama_produk[barang-1]
        del harga [barang-1]
        del jumlah_beli [barang-1]
        z+=1
        print ("Berhasil Terhapus")
    print ("===========================================================================================================")
    while s < f :
        print (s+1 , "\t Nama Produk : ", nama_produk[s] , "\t banyak : " , jumlah_beli[s],"\t Harga/1 :Rp", harga[s])
        s+=1
    print ("Jumlah Barang Yang Anda Beli : %i ".center(90)%f)
    print ("===========================================================================================================")
        
else :
    print ("===========================================================================================================")
    while s < jumlah_transaksi :
        print (s+1 , "\t Nama Produk : ", nama_produk[s] , "\t banyak : " , jumlah_beli[s],"\t Harga/1 :Rp", harga[s])
        s+=1
    print ("===========================================================================================================")

a=0
total_belanja = 0 
while a < jumlah_transaksi :
    total_belanja = total_belanja + jumlah_harga [a]
    a+=1
print ("Nama Pembeli :",nama)
print ("Total Belanjaan : Rp ",total_belanja)
uang_bayar = int(input("Masukan Jumlah Uang Bayar :Rp"))
uang_kembali = uang_bayar-total_belanja
print ("                  Uang Kembali :Rp",uang_kembali)
garis ()