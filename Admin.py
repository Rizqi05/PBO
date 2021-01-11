class Admin(User):
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def showInfo(self):
        query = "Select * from dataMahasiswa"
        cursor.execute(query)
        conn.fetchall()

    def tambahBuku(self):
        judulBuku = str(input("input judul buku baru : "))
        penulis = str(input("input penulis buku baru : "))
        lokasi = str(input("input lokasi buku baru : "))
        query = "insert into buku values('','{}','{}','{}')".format(judulBuku,penulis,lokasi)
        cursor.execute(query)
        conn.commit()
        print("\nberhasil menambahkan buku dengan data:\njudul buku : {}\npenulis : {}\nlokasi : {}\n".format(judulBuku,penulis,lokasi))

        
    def ubahBuku(self):
        judulBuku = str(input("input judul buku yang ingin dirubah : "))
        cekBuku = "select judul from buku where judul = '{}'".format(judulBuku)
        cursor.execute(cekBuku)
        cekBuku = cursor.fetchall()
        print("\nbuku ditemukan dengan judul :",cekBuku[0][0])

        adminInput = int(input("\nubah buku berdasarkan\n1. judul\n2. penulis\n3. lokasi\n4. back\ninput angka pilihan diatas : "))
        if adminInput == 1:
            try:
                judulBaru = str(input("input judul buku baru : "))
                query = "update buku set judul = '{}' where judul = '{}'".format(judulBaru,judulBuku)
                cursor.execute(query)
                conn.commit()
                print("\ndata buku berhasil dirubah :)\n")

            except:
                print("\njudul tersebut tidak ada!\n")
        elif adminInput == 2:
            try:
                penulisBaru = str(input("input penulis buku baru : "))
                query = "update buku set penulis = '{}' where judul = '{}'".format(penulisBaru,judulBuku)
                cursor.execute(query)
                conn.commit()
                print("\ndata buku berhasil dirubah :)\n")

            except:
                print("\njudul tersebut tidak ada!\n")
        elif adminInput == 3:
            try:
                lokasiBaru = str(input("input penulis buku baru : "))
                query = "update buku set lokasi = '{}' where judul = '{}'".format(lokasiBaru,judulBuku)
                cursor.execute(query)
                conn.commit()
                print("\ndata buku berhasil dirubah :)\n")

            except:
                print("\njudul tersebut tidak ada!\n")

        elif adminInput == 4:
            return True
    def rekapPengunjung(self):
        query = "select idMahasiswa,namaLengkap,username,email,bukuPinjamJudul,bukuPinjamPenulis,bukuPinjamLokasi from dataMahasiswa"
        cursor.execute(query)
        dataMahasiswa = cursor.fetchall()
        for i in dataMahasiswa:
            print(i)


    def cariBuku(self):
        userInput = int(input("\n1. cari buku berdasarkan id\n2. cari buku berdasarkan judul\n3. cari buku berdasarkan lokasi\n4. back\ninput angka pilihan diatas : "))

        if userInput == 1:
            inputBuku = int(input("masukan id buku : "))
            query = "select * from buku where idBuku = {}".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("\nid buku :",dataBuku[0])
                print("judul :",dataBuku[1])
                print("penulis buku :",dataBuku[2])
                print("lokasi buku :",dataBuku[3])
            except:
                print("\nid buku tidak ditemukan") 
        elif userInput == 2:
            inputBuku = str(input("masukan judul buku : "))
            query = "select * from buku where judul = '{}'".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("\nid buku :",dataBuku[0])
                print("judul :",dataBuku[1])
                print("penulis buku :",dataBuku[2])
                print("lokasi buku :",dataBuku[3])
            except:
                print("\njudul buku tidak ditemukan") 
        elif userInput == 3:
            inputBuku = str(input("masukan lokasi buku : "))
            query = "select * from buku where lokasi = '{}'".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("\nid buku :",dataBuku[0])
                print("judul :",dataBuku[1])
                print("penulis buku :",dataBuku[2])
                print("lokasi buku :",dataBuku[3])
            except:
                print("\nlokasi tidak ditemukan") 

        elif userInput == 4:
            return True