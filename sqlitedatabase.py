import sqlite3


con=sqlite3.connect("dersler.db")

cursor=con.cursor();

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS Ogrenciler(id INTEGER PRIMARY KEY AUTOINCREMENT ,ad VARCHAR(50),soyad VARCHAR(50),numara INT,ders_notu INT)")

def insertTable():
    cursor.execute("INSERT INTO Ogrenciler(ad,soyad,numara,ders_notu) VALUES ('Tunahan','Okunan',85,99)")
    con.commit()
    con.close()
    print("Eklendi..")

'''

def insertTable(_ad,_soyad,_numara,_ders_notu):
    cursor.execute("INSERT INTO Ogrenciler(ad,soyad,numara,ders_notu) VALUES(?,?,?,?)",(_ad,_soyad,_numara,_ders_notu))
    con.commit()
    con.close()
    print("Eklendi..")
    '''

def dataCek():
    cursor.execute("SELECT * FROM Ogrenciler")
    data=cursor.fetchall()
    #print(data)
    for i in data:
        print(i)

def updateTable(_ad,_soyad,_numara,_ders_notu,_id):
    cursor.execute("UPDATE Ogrenciler SET ad=?,soyad=?,numara=?,ders_notu=? where id=?",(_ad,_soyad,_numara,_ders_notu,_id))
    con.commit()
    con.close()
    print("Güncellendi..")

def deleteTable():
    cursor.execute("DROP TABLE Ogrenciler")
    con.commit()
    con.close()
    print("Silindi..")


#deleteTable()



#createTable()


#dataCek()
ad=input("Güncellenecek Adınızı Giriniz:")
soyad=input("Güncellenecek Soyadızı Giriniz:")
numara=input("Güncellenecek Numaranızı Giriniz:")
ders_notu=input("Güncellenecek Ders Notunuzu Giriniz")
id=input("Güncellenecek Id Giriniz")
updateTable(ad,soyad,numara,ders_notu,id)



'''
ad=input("Adınızı Giriniz:")
soyad=input("Soyadızı Giriniz:")
numara=input("Numaranızı Giriniz:")
ders_notu=input("Ders Notunuzu Giriniz")
insertTable(ad,soyad,numara,ders_notu)

'''
#insertTable()