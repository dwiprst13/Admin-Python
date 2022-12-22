# Program Admin Gudang Toko Hp Xiaomi
print()
print("="*45)
print("Selamat datang di Program Admin Sederhana")
print("="*45)

# Variabel Pokok
daftar = [   
            {'code': 'rn10', 'type': 'Redmi Note 10', 'quantity': 13, 'price': 1800500},    
            {'code': 'rn11', 'type': 'Redmi Note 11', 'quantity': 23, 'price': 2250000},       
            {'code': 'rn11p', 'type': 'Redmi Note 11 Pro', 'quantity': 9, 'price': 4150000}
        ]

print()
print("Daftar menu yang tersedia:")

menu = 1 
while menu != 0: 
    print("1. Lihat data di gudang")
    print("2. Lihat data produk")
    print("3. Meng-input barang masuk")
    print("4. Barang keluar")
    print("5. Menghapus produk dari daftar")
    print("6. Ubah harga barang")
    print("7. Cetak laporan Harian")
    print("0. Exit")
    menu = int(input("Masukan angka sesuai dengan yang anda pilih: "))
    print()

    if menu == 1: #Lihat data di gudang
        print("Lihat data di gudang")
        print('-'*70) 
        print("|", "%-8s"%"Kode"+"%-20s"%"Tipe"+"%-10s"%"Jumlah"+"%-12s"%"Harga(Rp)"+"%-16s"%"Jumlah Nilai(Rp)","|") 
        print('-'*70)
        total_value = 0
        for item in daftar:
            if item['quantity'] == 0:
                item['quantity'] = 'Habis'
            value = item['quantity'] * item['price']
            if value == 0:
                value = 'Habis'
            total_value += value
            print("|", "%-8s"% item['code'] + "%-20s"%item['type'] + "%-10s"%item['quantity'] + "%-12s"%'{:,}'.
            format(item['price']).replace(',', '.'),"%-15s"%'{:,}'.format(value).replace(',', '.'), "|")
        print('-'*70) 
        print("|","%-10s"%"Total:"+"%+41s"%"Rp: "+"%-15s"%'{:,}'.format(total_value).replace(',', '.'),"|")
        print('-'*70) 
        print()

    elif menu == 2: #Lihat data produk
        cek_code = input("Masukan kode barang: ")
        item = next((i for i in daftar if i['code'] == cek_code), None)
        if item:
            print(item['type'], "tersedia sebanyak", item['quantity'], "unit, dengan harga perunit sebesar: Rp", 
                item['price'])
            print("Nilai total dari", item['type'], "sebesar: Rp", (item['quantity']*item['price']))
            print()
        else:
            print("Barang dengan kode", cek_code, "tidak tersedia")
            print()

    elif menu == 3: #Meng-input barang masuk
        tambah_code = input("Masukan kode barang: ")
        item = next((i for i in daftar if i['code'] == tambah_code), None)
        if item:
            tambah_qty = int(input("Masukan jumlah barang yang akan ditambahkan: "))
            item['quantity'] += tambah_qty
            print("Jumlah barang", item['type'], "berhasil ditambahkan sebanyak", tambah_qty)
            print()
        else:
            tambah_type = input("Masukan tipe barang: ")
            tambah_qty = int(input("Masukan jumlah barang yang akan ditambahkan: "))
            tambah_price = int(input("Masukan harga barang: "))
            daftar.append({'code': tambah_code, 'type': tambah_type, 'quantity': tambah_qty, 'price': tambah_price})
            print("Barang baru berhasil ditambahkan")
            print()

    elif menu == 4: #Barang keluar
        keluar_code = input("Masukan kode barang: ")
        item = next((i for i in daftar if i['code'] == keluar_code), None)
        if item:
            keluar_qty = int(input("Masukan jumlah barang yang akan dikeluarkan: "))
            if item['quantity'] < keluar_qty:
                print("Jumlah barang yang tersedia tidak cukup")
            else:
                item['quantity'] -= keluar_qty
                print("Jumlah barang", item['type'], "berhasil dikeluarkan sebanyak", keluar_qty)
            print()
        else:
            print("Barang dengan kode", keluar_code, "tidak tersedia")
            print()

    elif menu == 5: #Menghapus produk dari daftar
        hapus_code = input("Masukan kode barang: ")
        item = next((i for i in daftar if i['code'] == hapus_code), None)
        if item:
            daftar.remove(item)
            print("Barang dengan kode", hapus_code, "berhasil dihapus dari daftar")
            print()
        else:
            print("Barang dengan kode", hapus_code, "tidak tersedia")
            print()

    elif menu == 6: #Ubah harga barang
        ubah_code = input("Masukan kode barang: ")
        item = next((i for i in daftar if i['code'] == ubah_code), None)
        if item:
            ubah_harga = int(input("Masukan harga baru: "))
            item['price'] = ubah_harga
            print("Harga barang", item['type'], "berhasil diubah menjadi", ubah_harga)
            print()
        else:
            print("Barang dengan kode", ubah_code, "tidak tersedia")
            print()

    elif menu > 0 and menu <= 6:
        print('Ada lagi yang akan anda lakukan?')

    elif menu == 0:
        print("Ok, See You!!! Goodbye!!")
        print()

    else:
        print("Masukan angka sesuai menu!!!")
        print()
        print("Daftar menu yang tersedia:")
