import requests
import time
from bs4 import BeautifulSoup
from termcolor import colored
import os



dosyaAdi=input("Dosya Adını Giriniz:")
todayDate=time.strftime("%d/%m/%Y")
todayDateDosya=time.strftime("%d_%m_%Y")
dosyaAdi=dosyaAdi + "_" + todayDateDosya

if os.path.isfile(dosyaAdi):
    print("dosya var")
else:
    print("dosya yok")




dosya=open(dosyaAdi,"a+",encoding='utf-8')

marketAdi="yenisey"
dolasilacakSayfa=1

durum = False

while True:
    url = "https://profil.gittigidiyor.com/"+marketAdi+"/aldigi-yorumlar/satis?sf=" + str(dolasilacakSayfa) + "#yorum"
    try:
        r = requests.get(url, timeout=10.0)
        soup = BeautifulSoup(r.content, "html.parser")
        soup.prettify("utf-8")
    except ConnectionError as e:
        print("Hata Connection Error:" + str(e))
        continue
    except TimeoutError as e:
        print("Hata Timeout:" + str(e))
        continue
    except requests.exceptions.TooManyRedirects as e:
        print("Hata TooManyRedirects:" + str(e))
        continue
    except requests.exceptions.RequestException as e:
        print("Hata RequestException:" + str(e))
        continue


    print(colored(str(dolasilacakSayfa) + ". Sayfadan Yorum Çekiliyor...","blue"))
    yorumlar = soup.find_all("p", {"class": "comment_content"})

    tarihler = soup.find_all("p",{"class":"mt10"})
    tarihListesi = []



    yorumSayac=0
    for tarih in tarihler:
            tarih = tarih.text
            if ("\n" not in tarih):
                if (todayDate == tarih):
                    tarihListesi.append(tarih)
                    cumle = yorumlar[yorumSayac].text.replace("\n", "")
                    cumle = cumle.strip()
                    yorumSayac=yorumSayac+1
                    if (cumle == "" or cumle == "\n"): continue
                    dosya.write(cumle + "\n")
                    print(""+cumle)

                else:
                    print("Bugünkü yorumlar çekilde dosyada")
                    durum=True


    if(durum==True):
        break
    dolasilacakSayfa=dolasilacakSayfa+1


