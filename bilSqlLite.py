import sqlite3

con=sqlite3.connect("bilbase.db")

cursor=con.cursor();

def insertTable(adi,cevap):
    cursor.execute("INSERT INTO bilmece(adi,cevap) VALUES ('"+adi+"','"+cevap+"')")
    con.commit()
    print("Eklendi..")

dosya = open("sorular.txt", "r", encoding='utf-8')

liste = []
liste2 = []

satirlar=dosya.readlines()
for satir in satirlar:
    liste.append(satir)
    print(satir)
dosya.close()

dosya2 = open("cevaplar.txt", "r", encoding='utf-8')

satirlarDosya2=dosya2.readlines()
for s2 in satirlarDosya2:
    liste2.append(s2)
    print(s2)
dosya2.close()




for i in range(0,200):
    insertTable(liste[i],liste2[i])
    print(liste[i] + " " + liste2[i] + " " + str(i))


con.close()




