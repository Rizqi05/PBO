import mysql.connector

conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="perpustakaan")
cursor=conn.cursor()  

class Admin:
    def __init__(self):
        pass
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
    

class Mahasiswa:
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

def login():
    for i in range(3):
        username = str(input("masukan username : "))
        if username == "admin":
            return "admin"
        password = str(input("masukan password : "))
        query = "select idMahasiswa from datamahasiswa where username = '{}' and password = '{}'".format(username,password)
        cursor.execute(query)   
        data = cursor.fetchall()

        try:
            id = data[0][0]
            return id
        except:
            print("username atau password yang anda masukan salah")
    print("\nanda telah gagal login sebanyak 3 kali")
def registrasi():
    namaLengkap = str(input("masukan nama lengkap : "))
    username = str(input("masukan username : "))
    email = str(input("masukan email : "))
    password = str(input("masukan password : "))
    query = "insert into datamahasiswa values ('','{}','{}','{}','{}',0,'belumPinjam','belumPinjam','belumPinjam')".format(namaLengkap,username,email,password)
    cursor.execute(query)
    conn.commit()
    print("\nselamat {}, anda berhasil registrasi, silahkan login\n".format(namaLengkap))

def programBerjalan():
    while True:
        main = int(input("\n1. login\n2. registrasi\n3. exit\ninput angka pilihan diatas : "))
        if main == 1:
            id = login()
            if id == "admin":
                admin = Admin
                while True:
                    adminInput = int(input("\n1. tambah buku\n2. ubah buku\n3. cari buku\n4. melihat rekap pengunjung\n5. logout\ninput angka pilihan diatas : "))
                    if adminInput == 1:
                        admin.tambahBuku("tambah buku")
                    elif adminInput == 2:
                        admin.ubahBuku("ubah buku")
                    elif adminInput == 3:
                        admin.cariBuku("cari buku")
                    elif adminInput == 4:
                        admin.rekapPengunjung("rekap pengunjung")
                    elif adminInput == 5:
                        programBerjalan()
            else:
                query = "select * from datamahasiswa where idMahasiswa = "+str(id)
                cursor.execute(query)
                data = cursor.fetchall()[0]
                pengunjung = Mahasiswa(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
                while True:
                    userInput = int(input("\n1. cari buku\n2. pinjam buku\n3. kembalikan buku\n4. logout\ninput angka pilihan diatas : "))
                    if userInput == 1:
                        pengunjung.cariBuku()
                    elif userInput == 2:
                        pengunjung.pinjamBuku()
                    elif userInput == 3:
                        pengunjung.kembalikanBuku()
                    elif userInput == 4:
                        programBerjalan()

        elif main == 2:
            registrasi()
        elif main == 3:
            exit("selamat datang kembali :)")
        else:
            print("pilihan tidak tersedia")

programBerjalan()