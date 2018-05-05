import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from termcolor import colored
import os


# GITTIGIDIYOR
def maxSayfaSayisiniBul():
    hata=0
    max = -1
    url = "https://profil.gittigidiyor.com/yenisey/aldigi-yorumlar/satis?sf=2#yorum"
    while(hata==0):
        try:
            hata=0
            r = requests.get(url, timeout=10.0)
            soup = BeautifulSoup(r.content, "html.parser")
            soup.encode('utf-8')
            soup.prettify("utf-8")
        except ConnectionError as e:
            hata=-1
            print("Base Connection Error:" + str(e))
        except TimeoutError as e:
            hata=-1
            print("Base Timeout:" + str(e))
        except requests.exceptions.TooManyRedirects as e:
            hata=-1
            print("Base TooManyRedirects:" + str(e))
        except requests.exceptions.RequestException as e:
            hata=-1
            print("Base RequestException:" + str(e))

        if(hata==-1):
            hata=0;
            continue
        alinan_url = ""

        for a in soup.find_all('a', href=True):
            alinan_url = a['href']
            if (alinan_url.__contains__("satis?sf=")):
                parsed_url = urlparse(alinan_url)
                sayfaSayisi = parse_qs(parsed_url.query)
                page = sayfaSayisi.get("sf")
                pageInt = (int)(page.__getitem__(0))

                # print(pageInt)
                if (pageInt > max):
                    max = pageInt

        hata=1

    return max



print("Maximum Sayfa Sayisi=" + str(maxSayfaSayisiniBul()))

dosyaAdi=input("Dosya Adını Giriniz:")
if os.path.isfile(dosyaAdi):
    print("dosya var")
else:
    print("dosya yok")

dosya=open(dosyaAdi,"a+",encoding='utf-8')
marketAdi=input("Market Adı giriniz:")

yorumSayisi = 0
liste = []
listeDate=[]

cumle = ""
maxSayfaSayisi= maxSayfaSayisiniBul()
tarih=""
dolasilacakSayfa=1
while(dolasilacakSayfa<=maxSayfaSayisiniBul()):
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
    #tarihler=soup.find_all("p",{"class":"mt10"})
    for yorum in yorumlar:
        cumle = yorum.text.replace("\n", "")
        cumle=cumle.strip()
        if (cumle == "" or cumle=="\n"): continue
        liste.append(cumle)
        dosya.write(cumle+"\n")
        yorumSayisi += 1
        print(cumle)

    dosya.flush();
    dolasilacakSayfa+=1

print("Toplam Yorum Sayisi=" + str(yorumSayisi))
dosya.close()


