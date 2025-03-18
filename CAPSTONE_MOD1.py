#################### CASE STUDY : PENJUALAN BARANG TOKO SEPATU SEMBILAN ###################
import json
# buka file JSON
file_json = open("Dataset.json")
file2_json = open("dataset_sendal.json") 

# prsing data JSON
data_sepatu = json.loads(file_json.read())
data_sendal = json.loads(file2_json.read())


def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return []

def save_to_json(data_sepatu):
    with open("Dataset.json", "w") as file:
        json.dump(data_sepatu, file, indent=4)
        # print("Data berhasil disimpan ke Dataset.json")

def melihat_data():
    dict_sepatu = load_data("dataset.json")  # Memuat data sepatu
    jumlah_data_sepatu = len(dict_sepatu)  # Data Sepatu
    print("\t\t\t\t DATABASE SEPATU TOKO SEMBILAN \n ")
    print("Index\t | Nama \t\t\t | Seri\t\t | Harga \t | Stock \t | Jenis \t | Toko Penyimpanan \t |")
    print("-------- |-------------------------------|---------------|---------------|---------------|---------------|-----------------------|")
    for i in range(jumlah_data_sepatu):
        print(f'''{i}\t | {dict_sepatu[i]["nama_sepatu"]}\t\t\t | {dict_sepatu[i]["seri"]}\t | {dict_sepatu[i]["harga_sepatu"]}\t | {dict_sepatu[i]["stock_sepatu"]}\t\t | {dict_sepatu[i]["jenis_sepatu"]}\t | {dict_sepatu[i]["toko"]}\t\t\t | ''')
    print("\n")

# FITUR SHOW DATA
def show_data():
    # dict_sepatu = load_data("dataset.json")  # Memuat data sepatu
    # dict_sendal = load_data("dataset_sendal.json")  # Memuat data sendal

    while True:
        print('''  SELAMAT DATANG DI MENU MELIHAT SEPATU !!!
            Silahkan Pilih Menu :
              1. Tampilkan Data
              2. Tampilkan Data Sepatu berdasarkan toko 
              0. Back To Main menu
    ''')
        input_user = input("Pilih angka berapa yang ingin anda tampilkan : ")
        print("\n")

        if input_user == "1":
            print("Pilih database yang ingin dibuka:")
            print("1. Database Sepatu")
            print("2. Database Sendal")
            input_db = input("Pilih database: ")

            # Memilih database sesuai input
            if input_db == "1":
                selected_database = data_sepatu #dict_sepatu  # Data Sepatu
                print("\t\t\t\t DATABASE SEPATU TOKO SEMBILAN \n ")
                print("Index\t | Nama \t\t\t | Seri\t\t | Harga \t | Stock \t | Jenis \t | Toko Penyimpanan \t |")
                print("-------- |-------------------------------|---------------|---------------|---------------|---------------|-----------------------|")
                for i in range(len(selected_database)):
                    print(f'''{i}\t | {selected_database[i]["nama_sepatu"]}\t\t\t | {selected_database[i]["seri"]}\t | {selected_database[i]["harga_sepatu"]}\t | {selected_database[i]["stock_sepatu"]}\t\t | {selected_database[i]["jenis_sepatu"]}\t | {selected_database[i]["toko"]}\t\t\t | ''')
                print("\n")
            elif input_db == "2":
                selected_database = data_sendal # Data Sendal
                if len(selected_database) == 0:
                    print("Data tidak ada")
                    print("\n")
            else:
                print("Pilihan tidak valid!")
                continue
            
        elif input_user == "2":
            input_toko_filter = input("Masukkan data gudang mana yang anda pilih (A / B) ? ").lower()
            print("\n")

            selected_database = data_sepatu #dict_sepatu 

            data_filter = []
            for i in selected_database:
                if input_toko_filter == i['toko'].lower():
                    data_filter.append(i)

            # Menambahkan pengecekan jika toko yang dipilih tidak ada data
            if len(data_filter) == 0:
                print("Data untuk toko yang dipilih tidak ada.")
            else:
                print("Index\t | Nama \t\t |SERI \t\t | Harga \t | Stock \t | Jenis \t | Toko Penyimpanan \t |")
                print("-------- |-----------------------|---------------|---------------|---------------|---------------|-----------------------|")
                for i in range(len(data_filter)):
                    print(f'''{i}\t | {data_filter[i]["nama_sepatu"]}\t\t |{selected_database[i]["seri"]}\t | {data_filter[i]["harga_sepatu"]}\t | {data_filter[i]["stock_sepatu"]}\t\t | {data_filter[i]["jenis_sepatu"]}\t | {data_filter[i]["toko"]}\t\t\t | ''')   
            print("\n")
        elif input_user == "0":
            print("Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid, silakan pilih opsi yang benar.")
            print("\n")

# FITUR MENAMBAH DATA
def add_data_sepatu():
    while True:
        print(''' Selamat datang di menu Tambah Sepatu !!! 
            Silahkan pilih :       
              1. Menambahkan Data 
              0. Kembali ke Menu Utama 
                ''')
        inputan_user = input("pilih menu no : ") 
        print('\n')

        if inputan_user == "1":
            # Mengoutputkan database sepatu 
            melihat_data()
            print('\n')
            # Inputan data sepatu
            print ('   SILAHKAN INPUTKAN DATA SEPATU YANG BARUU !! ')
            input_nama_sepatu = input("masukan nama sepatu : ")
            input_seri_sepatu = input("masukan seri sepatu : ")

            # Cek apakah data sepatu sudah ada langsung di dalam fungsi add_data_sepatu
            for item in data_sepatu:
                if item['nama_sepatu'] == input_nama_sepatu and item['seri'] == input_seri_sepatu:
                    print("Data sepatu dengan nama dan seri tersebut sudah ada.")
                    print("\n")  # Menampilkan pesan jika data sudah ada
                    break
            else:  # else ini untuk kasus jika tidak ada duplikasi, dan kita lanjutkan input berikutnya
                # Input data lainnya
                while True: 
                    try:
                        input_harga_sepatu = int(input("Masukan nominal harga sepatu : "))
                        break
                    except Exception as e :
                        print(e)
                        print ("Masukan dalam bentuk angka !!")
                  
                while True :
                    try:
                        input_stock_sepatu = int(input("Masukan stock sepatu : "))
                        break
                    except :
                        print ("Masukan dalam bentuk angka !!")

                input_jenis_sepatu = input("masukan jenis atau peruntukan sepatu tersebut (Sepatu kerja/ Sepatu main /Sepatu sport dll.) : ")
                input_toko_sepatu = input("masukan di toko mana sepatu tersebut akan di simpan toko sembilan (a / b): ")

               
                print(f"\nData yang akan ditambahkan:")
                print("Index\t | Nama \t\t\t | Seri\t\t | Harga \t | Stock \t | Jenis \t | Toko Penyimpanan \t |")
                print("-------- |-------------------------------|---------------|---------------|---------------|---------------|-----------------------|")
                print(f"{0}\t | {input_nama_sepatu}\t\t\t | {input_seri_sepatu}\t | {input_harga_sepatu}\t | {input_stock_sepatu}\t\t | {input_jenis_sepatu}\t | {input_toko_sepatu}\t\t\t | ")


                # Konfirmasi apakah ingin menambahkan data
                input_konfirmasi = input("\nApakah Anda ingin menambahkan data ini? (y/n): ").lower()
                
                if input_konfirmasi == 'y':
                    # Menambahkan data ke dictionary
                    dict_baru = {
                        "nama_sepatu": input_nama_sepatu, 
                        "seri" : input_seri_sepatu,
                        "harga_sepatu": input_harga_sepatu,
                        "stock_sepatu": input_stock_sepatu,
                        "jenis_sepatu": input_jenis_sepatu,
                        "toko": input_toko_sepatu
                    }
                    data_sepatu.append(dict_baru)  
                    save_to_json(data_sepatu)
                    print("Data telah di tambah !")
                    melihat_data()
                    print("\n")    
                elif input_konfirmasi == 'n':
                    print("Data tidak ditambahkan.")
                    print("\n")  
        elif inputan_user == "0":
            main_menu()
        else:
            print("Pilihan tidak valid, silakan pilih opsi yang benar.")
            print("\n")
# FITUR UPDATE DATA
def update_data_sepatu():
    while True:
        print('''
              Selamat datang di menu Update Data Sepatu !!!
                    Silahkan pilih :
                    1. Mengubah Data
                    0. Kembali ke Menu Utama
        ''')
        inputan_user = input("Pilih menu no: ")
        print("\n")
        if inputan_user == "1":
            melihat_data()
            input_update_user = int(input("Masukkan no index berapa yang ingin anda ubah: "))

            # Cek apakah indeks valid (PERUBAHAN)
            if input_update_user < 0 or input_update_user >= len(data_sepatu):
                print("Data yang Anda pilih tidak ada.")
                continue

            print(''' Pilih data yang ingin diubah:
                1. Nama Sepatu
                2. Harga Sepatu
                3. Stock Sepatu
                4. Jenis Sepatu
                5. Toko Penyimpan
                6. Seri Sepatu
            ''')
            input_update_nilai = input("Pilih field yang ingin diubah: ")

            if input_update_nilai == "1":
                nilai_baru = input("Masukkan nama sepatu baru: ")
                data_sepatu[input_update_user]["nama_sepatu"] = nilai_baru
                
                # Menampilkan data yang akan diubah
                print("\nData yang akan diperbarui:")
                print("|Nama \t\t|  ")
                print("|---------------|")
                print(f"|{data_sepatu[input_update_user]['nama_sepatu']}\t|")

                # Konfirmasi update data
                konfirmasi = input("\nApakah Anda ingin mengupdate data ini? (y/n): ").lower()
                if konfirmasi == 'y':
                    save_to_json(data_sepatu)  # Menyimpan perubahan ke file
                    print("Data Telah di update.")
                    melihat_data()  # Menampilkan database setelah update
                else:
                    print("Update dibatalkan.")
                    continue  # Kembali ke menu atau ulangi

            elif input_update_nilai == "2":
                try:
                    nilai_baru = int(input("Masukkan harga sepatu baru: "))
                    data_sepatu[input_update_user]["harga_sepatu"] = nilai_baru
                    
                    # Menampilkan data yang akan diubah
                    print("\nData yang akan diperbarui:")
                    print("|Harga\t\t |  ")
                    print("|----------------|")
                    print(f"|{data_sepatu[input_update_user]['harga_sepatu']}\t| ")

                    # Konfirmasi update data
                    konfirmasi = input("\nApakah Anda ingin mengupdate data ini? (y/n): ").lower()
                    if konfirmasi == 'y':
                        save_to_json(data_sepatu)  # Menyimpan perubahan ke file
                        print("Data Telah di update.")
                        melihat_data()  # Menampilkan database setelah update
                    else:
                        print("Update dibatalkan.")
                        continue  # Kembali ke menu atau ulangi
                except:
                    print("Masukan dalam bentuk angka !!")

            elif input_update_nilai == "3":
                try:
                    nilai_baru = int(input("Masukkan stock sepatu baru: "))
                    data_sepatu[input_update_user]["stock_sepatu"] = nilai_baru
                    
                    # Menampilkan data yang akan diubah
                    print("\nData yang akan diperbarui:")
                    print("|Stock \t\t |  ")
                    print("|----------------|")
                    print(f"|{data_sepatu[input_update_user]['stock_sepatu']}\t| ")

                    # Konfirmasi update data
                    konfirmasi = input("\nApakah Anda ingin mengupdate data ini? (y/n): ").lower()
                    if konfirmasi == 'y':
                        save_to_json(data_sepatu)  # Menyimpan perubahan ke file
                        print("Data Telah di update.")
                        melihat_data()  # Menampilkan database setelah update
                    else:
                        print("Update dibatalkan.")
                        continue  # Kembali ke menu atau ulangi
                except:
                    print('Masukan dalam bentuk angka !!')

            elif input_update_nilai == "4":
                nilai_baru = input("Masukkan jenis sepatu baru: ")
                data_sepatu[input_update_user]["jenis_sepatu"] = nilai_baru
                
                # Menampilkan data yang akan diubah
                print("\nData yang akan diperbarui:")
                print("|Jenis\t\t|  ")
                print("|---------------|")
                print(f"|{data_sepatu[input_update_user]['jenis_sepatu']}\t| ")

                # Konfirmasi update data
                konfirmasi = input("\nApakah Anda ingin mengupdate data ini? (y/n): ").lower()
                if konfirmasi == 'y':
                    save_to_json(data_sepatu)  # Menyimpan perubahan ke file
                    print("Data Telah di update.")
                    melihat_data()  # Menampilkan database setelah update
                else:
                    print("Update dibatalkan.")
                    continue  # Kembali ke menu atau ulangi

            elif input_update_nilai == "5":
                nilai_baru = input("Masukkan nama toko penyimpanan baru: ")
                data_sepatu[input_update_user]["toko"] = nilai_baru
                
                # Menampilkan data yang akan diubah
                print("\nData yang akan diperbarui:")
                print("|Toko\t\t |  ")
                print("|---------------|")
                print(f"|{data_sepatu[input_update_user]['toko']}\t|")

                # Konfirmasi update data
                konfirmasi = input("\nApakah Anda ingin mengupdate data ini? (y/n): ").lower()
                if konfirmasi == 'y':
                    save_to_json(data_sepatu)  # Menyimpan perubahan ke file
                    print("Data Telah di update.")
                    melihat_data()  # Menampilkan database setelah update
                else:
                    print("Update dibatalkan.")
                    continue  # Kembali ke menu atau ulangi

            elif input_update_nilai == "6":
                while True:
                    nilai_baru = input("Masukkan seri sepatu baru: ")
                    # Memeriksa apakah seri sepatu baru sudah ada dalam database
                    if any(item['seri'] == nilai_baru for item in data_sepatu):
                        print("Seri sepatu ini sudah ada. Mohon masukkan seri yang berbeda.")
                    else:
                        data_sepatu[input_update_user]["seri"] = nilai_baru
                        break
                
                # Menampilkan data yang akan diperbarui
                print("\nData yang akan diperbarui:")
                print(" |Seri \t\t |  ")
                print("|----------------------|")
                print(f"|{data_sepatu[input_update_user]['seri']}\t\t ")

                # Konfirmasi update data
                konfirmasi = input("\nApakah Anda ingin mengupdate data ini? (y/n): ").lower()
                if konfirmasi == 'y':
                    save_to_json(data_sepatu)  # Menyimpan perubahan ke file
                    print("Data Telah di update.")
                    melihat_data()  # Menampilkan database setelah update
                else:
                    print("Update dibatalkan.")
                    continue  # Kembali ke menu atau ulangi

            else:
                print("Pilihan tidak valid.")
                
        elif inputan_user == "0":
            main_menu()
        else:
            print("Pilihan tidak valid, silakan pilih opsi yang benar.")
            print("\n")

#FITUR MENGHAPUS DATA
def delete_data_sepatu():
    while True:
        print('''
              Selamat datang di menu Hapus Data Sepatu !!!
                    Silahkan pilih :       
                    1. Menghapus Data 
                    0. Kembali ke Menu Utama 
        ''')
        inputan_user = input("Pilih menu no : ") 
        if inputan_user == "1":
            try:
                melihat_data()  # Menampilkan data yang ada
                input_hapus_user = int(input("Masukkan no index berapa yang ingin anda hapus : "))

                # Cek apakah data yang dipilih ada dalam data_sepatu
                if input_hapus_user < 0 or input_hapus_user >= len(data_sepatu):
                    print("Index yang Anda pilih tidak ada, mohon masukkan index yang valid.")
                    continue

                # Menampilkan data yang akan dihapus
                print("\nData yang akan dihapus:")
                print("Index\t | Nama \t\t\t | Seri\t\t | Harga \t | Stock \t | Jenis \t | Toko Penyimpanan \t |")
                print("-------- |-------------------------------|---------------|---------------|---------------|---------------|-----------------------|")
                print(f"{input_hapus_user}\t | {data_sepatu[input_hapus_user]['nama_sepatu']}\t\t\t | {data_sepatu[input_hapus_user]['seri']}\t | {data_sepatu[input_hapus_user]['harga_sepatu']}\t | {data_sepatu[input_hapus_user]['stock_sepatu']}\t\t | {data_sepatu[input_hapus_user]['jenis_sepatu']}\t | {data_sepatu[input_hapus_user]['toko']}\t\t\t |")

                # Meminta konfirmasi dari pengguna
                konfirmasi = input("\nApakah Anda ingin menghapus data ini? (y/n): ").lower()
                if konfirmasi == 'y':
                    # Menghapus data yang dipilih
                    del data_sepatu[input_hapus_user]
                    save_to_json(data_sepatu)  # Menyimpan perubahan ke file JSON
                    print("Data berhasil dihapus.")
                    melihat_data()  # Menampilkan data yang sudah diupdate
                else:
                    print("Penghapusan data dibatalkan.")
                    continue  # Kembali ke menu atau ulangi
            except ValueError:
                print("Masukkan index yang valid, berupa angka.")
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
        elif inputan_user == "0":
            main_menu()  # Kembali ke menu utama
        else:
            print("Pilih inputan yang sesuai dengan menu yang tertera")

#MAIN MENU
def main_menu():
    while True :
        print('''
                    SELAMAT DATANG DI WEREHOUSE TOKO SEMBILAN SEPATU !! \n
        Silahkan Pilih Fitur Yang di butuhkan :
            1. Menampilkan Data
            2. Menambahkan Data 
            3. Menghapus Data
            4. Update Data 
            0. Keluar dari Program 
        ''')
        input_user = input("\t Silahkan pilih fitur yang ingin digunakan : ")
        if input_user == '1':
            show_data()
        elif input_user == '2':
            add_data_sepatu()
        elif input_user == '3':
            delete_data_sepatu()
            print("")
        elif input_user == '4' :
            update_data_sepatu()
        elif input_user == '0':
            input_dari_user = input("Apakah anda ingin keluar program : (y/n)").lower()
            if input_dari_user == "y":
                save_to_json(data_sepatu)
                quit()
            else:
                main_menu()
        else:
            print("masukan inputan dengan benar ,silahkan memilih angka yang tersedia pada menu")
main_menu()