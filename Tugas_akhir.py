from datetime import datetime
id_produk       = []
nama_produk     = []
harga           = []
jumlah_beli     = []
jumlah_harga    = []
uang_bayar      = []
uang_kembali    = []
total_belanja   = []
jumlah_transaksi= []
transaksi       = []
nama = input ("Masukan Nama Pembeli :")
while True : 
    print("==========================================")
    print ("SELAMAT DATANG DI TOKO OBAT STUTLE")
    print("==========================================")
    print ("1.List Obat \n2.Beli Obat \n3.Hapus Obat \n4.Melihat Daftar Keranjang \n5.Transaksi Checkout")
    print ("_________________________________________")
    print("----------------------------------------")
    pilihan = (int(input("Masukan Pilihan Anda :")))
    print("----------------------------------------")
    if pilihan == 1 :
        print ("______________________________________________")
        print ("  ID PRODUK  |     NAMA PRODUK     |  HARGA   ")
        print ("      1      |  ANTISEPTIK         |  Rp.10000")
        print ("      2      |  OBAT FLU           |  Rp.5000 ")
        print ("      3      |  VITAMIN/SUPLEMENT  |  Rp.7500 ")
        print ("      4      |  TETES MATA         |  Rp.15000")
        print ("      5      |  PARACETAMOL        |  Rp.3000 ")
    elif pilihan == 2 : 
        transaksi =  int (input ("Masukan Jumlah Transaksi :"))
        jumlah_transaksi.append(transaksi)
        i = 0
        while i < transaksi :
            print ("Data ke-",i+1)
            id_produk.append(int(input("Masukan ID Produk :")))
            jumlah_beli.append(int(input("Masukan Jumlah Beli :")))
            if id_produk[i]== 1 :
                nama_produk.append("ANTISEPTIK              ")
                harga.append(10000)
                jumlah_harga.append(jumlah_beli[i]*int(10000))
            elif id_produk[i]== 2 :
                nama_produk.append("OBAT FLU                ")
                harga.append(5000)
                jumlah_harga.append(jumlah_beli[i]*int(5000))
            elif id_produk[i]== 3 :
                nama_produk.append("VITAMIN/SUPLEMENT       ")
                harga.append(7500)
                jumlah_harga.append(jumlah_beli[i]*int(7500))
            elif id_produk[i]== 4 :
                nama_produk.append("TETES MATA              ")
                harga.append(15000)
                jumlah_harga.append(jumlah_beli[i]*int(15000))
            elif id_produk[i]== 5 :
                nama_produk.append("PARACETAMOL             ")
                harga.append(3000)
                jumlah_harga.append(jumlah_beli[i]*int(3000))
            else :
                nama_produk.append("ID TIDAK ADA            ")
                harga.append(0)
                jumlah_harga.append(jumlah_beli[i]*int(0))
            i+=1
    elif pilihan == 3 :
            if len (jumlah_transaksi) != 0 :
                hapus = input ("Apakah Anda Ingin Menghapus Pesanan ? (Y/N):")
                if hapus == "y" or hapus == "Y" :
                    Banyak = int(input("Berapa Banyak Yang Ingin Anda Hapus ? :"))
                    z = 0
                    while z < Banyak :
                        g = 1
                        while g < len(nama_produk) :
                            for id in nama_produk :
                                print (g,"Nama Produk :" ,id)
                                g+=1
                        barang = int(input("Silahkan Ketik Urutan Yang Ingin Anda hapus :"))
                        del nama_produk[barang-1]
                        del harga [barang-1]
                        del jumlah_beli [barang-1]
                        del jumlah_harga [barang-1]
                        del id_produk[barang-1]
                        z+=1
                        print ("Berhasil Terhapus")
                        print ("===============================================================")
                else :
                    pass   
            else :
                print ("Tidak Ada Transaksi")
    elif pilihan == 4 :
        e = len(nama_produk)
        a = 0
        print("----------------------------------")
        print("DAFTAR BELANJA ANDA")
        print("----------------------------------")
        print ("Jumlah Barang Yang Anda Beli :" ,e)
        while a < e :
            print (a+1, "\t Nama Produk : ", nama_produk[a] , "\t banyak : " , jumlah_beli[a],"\t Harga/1 :Rp", harga[a],"\t Jumlah :", jumlah_harga[a])
            a+=1
    
    elif pilihan == 5 :
        tanggal = datetime.now()
        e = len(nama_produk)
        a=0
        total_belanja = 0 
        while a < e :
            total_belanja = total_belanja + jumlah_harga [a]
            a+=1
        print ("Nama Pembeli :",nama)
        print ("Total Belanjaan : Rp ",total_belanja)
        uang_bayar = int(input("Masukan Jumlah Uang Bayar :Rp "))
        uang_kembali = uang_bayar-total_belanja
        print ("                  Uang Kembali :Rp.",uang_kembali)
        print ("                  Tanggal :", tanggal)
        exit ()
    else : 
        print ("Menu Yang Anda Pilih Tidak Ada")
        pass