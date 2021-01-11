class Mahasiswa (User):
    def __init__(self,idMahasiswa,namaLengkap,username,email,password,bukuPinjamId,bukuPinjamJudul,bukuPinjamPenulis,bukuPinjamLokasi):
        self.__idMahasiswa = idMahasiswa
        self.__namaLengkap = namaLengkap
        self.__username = username
        self.__email = email
        self.__password = password
        self.__bukuPinjamId = bukuPinjamId
        self.__bukuPinjamJudul = bukuPinjamJudul
        self.__bukuPinjamPenulis = bukuPinjamPenulis
        self.__bukuPinjamLokasi = bukuPinjamLokasi
    
    def showInfo(self):
        print("nama\t\t= {}\nbuku pinjam\t= {}".format(self.__namaLengkap,self.__bukuPinjamId))


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

    def pinjamBuku(self):
            userInput = int(input("\n1. pinjam buku berdasarkan id\n2. pinjam buku berdasarkan judul\n3. pinjam buku berdasarkan lokasi\n4. back\ninput angka pilihan diatas : "))
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

                    self.__bukuPinjamId = dataBuku[0]
                    self.__bukuPinjamJudul = dataBuku[1]
                    self.__bukuPinjamPenulis = dataBuku[2]
                    self.__bukuPinjamLokasi = dataBuku[3]

                    query = "delete from buku where idBuku = {}".format(dataBuku[0])
                    cursor.execute(query)
                    conn.commit()
                    print("\nbuku berhasil dipinjam :)\n")
                    self.commit()

                except:
                    print("id buku tidak ditemukan") 
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

                    self.__bukuPinjamId = dataBuku[0]
                    self.__bukuPinjamJudul = dataBuku[1]
                    self.__bukuPinjamPenulis = dataBuku[2]
                    self.__bukuPinjamLokasi = dataBuku[3]
                    query = "delete from buku where idBuku = {}".format(dataBuku[0])
                    cursor.execute(query)
                    conn.commit()
                    print("\nbuku berhasil dipinjam :)\n")
                    self.commit()
                except:
                    print("judul buku tidak ditemukan") 
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

                    self.__bukuPinjamId = dataBuku[0]
                    self.__bukuPinjamJudul = dataBuku[1]
                    self.__bukuPinjamPenulis = dataBuku[2]
                    self.__bukuPinjamLokasi = dataBuku[3]
                    query = "delete from buku where idBuku = {}".format(dataBuku[0])
                    cursor.execute(query)
                    conn.commit()
                    print("\nbuku berhasil dipinjam :)\n")
                    self.commit()
                except:
                    print("lokasi tidak ditemukan") 

            elif userInput == 4:
                return True

    def kembalikanBuku(self):
        if self.__bukuPinjamJudul == "belum pinjam":
            print("\nanda tidak meminjam buku apapun")
            return True
        else:
            print("\nmengembalikan buku dengan data :")
            print("id buku :",self.__bukuPinjamId)
            print("judul buku :",self.__bukuPinjamJudul)
            print("penulis buku :",self.__bukuPinjamPenulis)
            print("lokasi buku :",self.__bukuPinjamLokasi)
            print()
            query = "insert into buku values({},'{}','{}','{}')".format(self.__bukuPinjamId,self.__bukuPinjamJudul,self.__bukuPinjamPenulis,self.__bukuPinjamLokasi)
            cursor.execute(query)
            conn.commit()
            print("buku berhasil dikembalikan")
            self.__bukuPinjamId = 0
            self.__bukuPinjamJudul = "belum pinjam"
            self.__bukuPinjamPenulis = "belum pinjam"
            self.__bukuPinjamLokasi = "belum pinjam"
            self.commit()

    def commit(self):
        query = "update dataMahasiswa set bukuPinjamid = {},bukuPinjamJudul = '{}',bukuPinjamPenulis = '{}',bukuPinjamLokasi = '{}' where idMahasiswa = {}".format(self.__bukuPinjamId,self.__bukuPinjamJudul,self.__bukuPinjamPenulis,self.__bukuPinjamLokasi,self.__idMahasiswa)
        cursor.execute(query)
        conn.commit()