def login():
    for i in range(3):
        username = str(input("masukan username : "))
        password = str(input("masukan password : "))
        if password == "admin":
            return "admin"
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