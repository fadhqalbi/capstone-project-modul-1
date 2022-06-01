daftar_mobil = {'B 41 K': {'nopol':'B 41 K','tipe':'Jeep','warna':'Merah','pemilik':'Ciko','kontak':'087521036975','status':'Sedia','biaya':450000},
                'B 46 US': {'nopol':'B 46 US','tipe':'Mini Bus','warna':'Abu-Abu','pemilik':'Dina','kontak':'082136985621','status':'Dalam Servis','biaya':375000}}
# daftar_mobil = {}

def menu_utama():
    global req
    req = int(input('''
++++SELAMAT DATANG DI GLOBAL RENT CAR++++

Pilihan Menu:
    1. Menampilkan Data Mobil
    2. Menambah Data Mobil
    3. Memperbaharui Data Mobil
    4. Menghapus Data Mobil
    5. Keluar
        
Silahkan masukkan angka Menu yang ingin anda jalankan: '''))
    return req


def tampilkan(data):
    print('\nDaftar Mobil di Global Rent Car: ')
    print('-'*120)
    print('Indeks\t | No.Polisi\t | Tipe \t | Warna\t | Pemilik\t | Kontak \t | Status \t | Biaya Sewa')
    print('-'*120)
    for i in range(len(data)):
        print('{}\t | {}\t | {}  \t | {} \t | {}  \t | {}\t | {}\t | {}'.format(i+1,data[i]['nopol'],data[i]['tipe'],data[i]['warna'],data[i]['pemilik'],data[i]['kontak'],data[i]['status'],data[i]['biaya']))
    print('-'*120)

def menu_read(opsi):
    while True:
        opsi = int(input('''
------------------------------------------------------------------------------------------------
Pilihan menampilkan data:
    1. Tampilkan semua data mobil
    2. Lihat mobil dengan nomor polisi
    3. Kembali ke Menu Utama

Untuk menampilkan data, silahkan masukkan angka Pilihan yang ingin dijalankan: '''.format(opsi)))

        if(opsi == 1):
            if(len(daftar_mobil) > 0):
                tampilkan(list(daftar_mobil.values()))
                break
            else:
                print('\n<<< Tidak ada data mobil yang tersimpan >>>')
        elif(opsi == 2):
            if(len(daftar_mobil) > 0):
                cari_nopol = str(input('\nMasukkan nomor polisi mobil: ')).upper()
                if (cari_nopol in daftar_mobil):
                    tampilkan([daftar_mobil[cari_nopol]])
                else:
                    print('\n<<< Mobil yang anda cari tidak ada di dalam database >>>')
            else:
                print('\n<<< Tidak ada data mobil yang tersimpan >>>')
        elif(opsi == 3):
            break

def menu_create(opsi):
    while True:
        opsi = str(input('''
------------------------------------------------------------------------------------------------
Apakah anda ingin menambahkan data mobil?(y/n) : '''))
        if (opsi == 'y'):
            nopol_baru = str(input('\nMasukkan Nomor Polisi : ')).upper()
            if (nopol_baru in daftar_mobil):
                print('\n<<< Data mobil dengan nomor polisi {} sudah tersimpan di database >>>'.format(nopol_baru))
            else:
                tipe_baru = str(input('\nMasukkan Tipe Mobil: ')).capitalize()
                warna_baru = str(input('Masukkan Warna Mobil: ')).capitalize()
                pemilik_baru = str(input('Masukkan Nama Pemilik Mobil: ')).capitalize()
                kontak_baru = str(input('Masukkan Kontak Pemilik Mobil: '))
                status_baru = str(input('Masukkan Status Mobil Saat Ini: ')).capitalize()
                biaya_baru = int(input('Masukkan Biaya Sewa Mobil: '))
                simpan = str(input('\nApakah anda ingin menyimpan data? (y/n) : '))
                if(simpan == 'y'):
                    daftar_mobil.update({nopol_baru:{'nopol':nopol_baru,'tipe':tipe_baru,'warna':warna_baru,'pemilik':pemilik_baru,'kontak':kontak_baru,'status':status_baru,'biaya':biaya_baru}})
                    print('\n<<< Data Berhasil Disimpan >>>')
                else:
                    print('\n<<< Data Belum Tersimpan >>>')
                    menu_create(daftar_mobil)
        elif(opsi == 'n'):
            break
        else:
            pass

def menu_update(opsi):
    while True:
        opsi = str(input('''
------------------------------------------------------------------------------------------------
Apakah anda ingin memperbaharui data mobil?(y/n) : '''))
        if (opsi == 'y'):
            cari_nopol = str(input('\nMasukkan Nomor Polisi : ')).upper()
            if (cari_nopol in daftar_mobil):
                tampilkan([daftar_mobil[cari_nopol]])
                kolom = int(input('''
Indeks kolom:
    1. Tipe Mobil
    2. Warna Mobil
    3. Nama Pemilik Mobil
    4. Kontak Pemilik Mobil
    5. Status Mobil
    6. Biaya Sewa Mobil
    7. Semua Kolom

Masukkan indeks kolom data yang ingin diperbaiki: '''))
    
                if(kolom == 1):
                    data_update = input('\nMasukkan Tipe Mobil yang Baru: ')
                    simpan = str(input('\nApakah anda ingin menyimpan data? (y/n) : '))
                    if(simpan == 'y'):
                        daftar_mobil[cari_nopol]['tipe'] = str(data_update).capitalize()
                        print('\n<<< Data Berhasil Disimpan >>>')
                    else:
                        print('\n<<< Data Belum Tersimpan >>>')
                elif(kolom == 2):
                    data_update = input('\nMasukkan Warna Mobil yang Baru: ')
                    simpan = str(input('\nApakah anda ingin menyimpan data? (y/n) : '))
                    if(simpan == 'y'):
                        daftar_mobil[cari_nopol]['warna'] = str(data_update).capitalize()
                        print('\n<<< Data Berhasil Disimpan >>>')
                    else:
                        print('\n<<< Data Belum Tersimpan >>>')                  
                elif(kolom == 3):
                    data_update = input('\nMasukkan Nama Pemilik Mobil yang Baru: ')
                    simpan = str(input('\nApakah anda ingin menyimpan data? (y/n) : '))
                    if(simpan == 'y'):
                        daftar_mobil[cari_nopol]['pemilik'] = str(data_update).capitalize()
                        print('\n<<< Data Berhasil Disimpan >>>')
                    else:
                        print('\n<<< Data Belum Tersimpan >>>')                  
                elif(kolom == 4):
                    data_update = input('\nMasukkan Kontak Pemilik Mobil yang Baru: ')
                    simpan = str(input('\nApakah anda ingin menyimpan data? (y/n) : '))
                    if(simpan == 'y'):
                        daftar_mobil[cari_nopol]['kontak'] = str(data_update).capitalize()
                        print('\n<<< Data Berhasil Disimpan >>>')
                    else:
                        print('\n<<< Data Belum Tersimpan >>>')                  
                elif(kolom == 5):
                    data_update = input('\nMasukkan Status Mobil yang Baru: ')
                    simpan = str(input('\nApakah anda ingin menyimpan data? (y/n) : '))
                    if(simpan == 'y'):
                        daftar_mobil[cari_nopol]['status'] = str(data_update).capitalize()
                        print('\n<<< Data Berhasil Disimpan >>>')
                    else:
                        print('\n<<< Data Belum Tersimpan >>>')                  
                elif(kolom == 6):
                    data_update = input('\nMasukkan Biaya Sewa Mobil yang Baru: ')
                    simpan = str(input('\nApakah anda ingin menyimpan data? (y/n) : '))
                    if(simpan == 'y'):
                        daftar_mobil[cari_nopol]['biaya'] = int(data_update)
                        print('\n<<< Data Berhasil Disimpan >>>')
                    else:
                        print('\n<<< Data Belum Tersimpan >>>')                  
                elif (kolom == 7):
                    tipe_baru = str(input('\nMasukkan Tipe Mobil: ')).capitalize()
                    warna_baru = str(input('Masukkan Warna Mobil: ')).capitalize()
                    pemilik_baru = str(input('Masukkan Nama Pemilik Mobil: ')).capitalize()
                    kontak_baru = str(input('Masukkan Kontak Pemilik Mobil: '))
                    status_baru = str(input('Masukkan Status Mobil Saat Ini: ')).capitalize()
                    biaya_baru = int(input('Masukkan Biaya Sewa Mobil: '))
                    simpan = str(input('\nApakah anda ingin menyimpan data? (y/n) : '))
                    if(simpan == 'y'):
                        daftar_mobil.update({cari_nopol:{'nopol':cari_nopol,'tipe':tipe_baru,'warna':warna_baru,'pemilik':pemilik_baru,'kontak':kontak_baru,'status':status_baru,'biaya':biaya_baru}})
                        print('\n<<< Data Berhasil Disimpan >>>')
                    else:
                        print('\n<<< Data Belum Tersimpan >>>')
                else:
                    print('\n<<< Silahkan masukkan indeks kolom yang tersedia >>>')
            else:
                print('\n<<< Tidak ada data mobil dengan nomor polisi {} >>>'.format(cari_nopol))
        elif(opsi == 'n'):
            break
        else:
            pass

def menu_delete(opsi):
    while True:
        opsi = str(input('''
------------------------------------------------------------------------------------------------
Apakah anda ingin menghapus data mobil?(y/n) : '''))
        if (opsi == 'y'):
            cari_nopol = str(input('\nMasukkan Nomor Polisi : ')).upper()
            if cari_nopol in daftar_mobil:
                tampilkan([daftar_mobil[cari_nopol]])
                hapus = str(input('Apakah anda ingin menghapus mobil ini? (y/n) : '))
                if(hapus == 'y'):
                    del daftar_mobil[cari_nopol]
                    print('\n<<< Data Berhasil Dihapus >>>')
                else:
                    print('\n<<< Data Belum Dihapus >>>')
            else:
                print('\n<<< Tidak ada data mobil dengan nomor polisi {} >>>'.format(cari_nopol))
        elif(opsi == 'n'):
            break
        else:
            pass

def menu_keluar():
    print('\n<<< Anda Telah keluar dari Aplikasi Global Rent Car. Semoga Hari Anda Menyenangkan! >>>')
    print('\n')
    exit()


while True:
    req = menu_utama()
    if(req == 1):
        menu_read(daftar_mobil)
    elif(req == 2):
        menu_create(daftar_mobil)
    elif(req == 3):
        menu_update(daftar_mobil)
    elif(req == 4):
        menu_delete(daftar_mobil)
    elif(req == 5):
        menu_keluar()
    else:
        print('\n<<< Silahkan masukkan indeks menu yang tersedia >>>')
