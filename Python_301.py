# FONSIYONLAR

# Matematiksel Islemler

4*4
4/4
5-1
6+3
3**2
3**3


#Fonksiyon Nasil Yazilir?

4**2 

def kare_al(x): 
    print(x**2) 
    
kare_al(5)    # 25 sonucunu verdi

# Bilgi Notuyla Cikti Uretmek

def kare_al(x):
    print(x**2)
    
kare_al(5)  

def kare_al(x):
    print("Girilen Sayinin Karesi:" + str(x**2))

kare_al(3)

def kare_al(x):
    print("Girilen Sayi:" + 
          str(x) + 
          ", Karesi:" +
          str(x**2))

kare_al(3)


# Iki Argumanli Fonksiyon Tanimlamak

def kare_al(x):
    print(x**2)
    
    
def carpma_yap(x, y):
    print(x*y)
    
carpma_yap(2,3)


# On Tanimli Argumanlar

# ?print

def carpma_yap(x, y = 1):
    print(x*y)

carpma_yap(3,4)

print("HELLO AI ERA")


# Argumanlarin Siralamasi

def carpma_yap(x, y = 1):
    print(x*y)

carpma_yap(y = 2, x = 3)

carpma_yap(2,3)




# Ne Zaman Fonksiyon Yazilir?

# Belediye Lamba Örneği

# isi, nem, sarj

(40+25)/90


def direk_hesap(isi, nem, sarj):
    print((isi + nem)/sarj)

direk_hesap(25,40,70)

# Ciktiyi Girdi Olarak Kullanmak

def direk_hesap(isi, nem, sarj):
    print((isi + nem)/sarj)

cikti = direk_hesap(25,40,70)

cikti

print(cikti)

direk_hesap(25,40,70)*9


def direk_hesap(isi, nem, sarj):
    return (isi + nem)/sarj


cikti = direk_hesap(25,40,70)

cikti

print(cikti)

direk_hesap(25,40,70)*9

def direk_hesap(isi, nem, sarj):
    return                          # Fonk. return ifadesine gelince durur.
    (isi + nem)/sarj


direk_hesap(25,40,70)



# Local ve Global Degiskenler

x = 10
y = 20

def carpma_yap(x = 2,y = 1):
    return x*y

carpma_yap(2,3) 


# Local Etki Alanindan Global Etki Alanini Degistirmek


x = []
#del x

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi")

eleman_ekle("ali") 

eleman_ekle("veli") 


# KARAR & KONTROL YAPILARI


# True-False Sorgulamaları

sinir = 5000 

sinir == 4000 

sinir == 5000 


5 == 4

5 == 5


# if

sinir = 50000
gelir = 60000

gelir < sinir

if gelir < sinir:
    print("Gelir sinirdan kucuk")
    
if gelir > sinir:
    print("Gelir sinirdan kucuk")
  

# else

sinir = 50000
gelir = 35000
    
if gelir > sinir:
    print("Gelir sinirdan buyuk")
else:
    print("Gelir sinirdan kucuk")    

# diger ornek

sinir = 50000
gelir = 50000
    
if gelir == sinir:
    print("Gelir sinira esittir")
else:
    print("Gelir sinira esit degildir")  

# elif

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000
    
if gelir1 > sinir:
    print("Tebrikler, hediye kazandiniz.")
elif gelir1 < sinir:
    print("Uyari!")
else:
    print("Takibe devam")  


if gelir3 > sinir:
    print("Tebrikler, hediye kazandiniz.")
elif gelir3 < sinir:
    print("Uyari!")
else:
    print("Takibe devam")  


if gelir2 > sinir:
    print("Tebrikler, hediye kazandiniz.")
elif gelir2 < sinir:
    print("Uyari!")
else:
    print("Takibe devam")  

# mini uygulama
sinir = 50000
magaza_adi = input("Magaza Adi Nedir?")
gelir = int(input("Gelirinizi Giriniz:"))

if gelir > sinir:
    print("Tebrikler:" + magaza_adi + " promosyon kazandiniz!")
elif gelir < sinir:
    print("Uyari! Cok dusuk gelir:" + str(gelir))
else:
    print("Takibe devam")



# DONGULER - for

ogrenci = ["ali","veli","isik","berk"]

ogrenci[0]
ogrenci[1]
ogrenci[2]
ogrenci[3]

for i in ogrenci:
    print(i)

# for ile baska bir örnek 

maaslar = [1000,2000,3000,4000,5000]

maaslar[0] 
maaslar[1] 
maaslar[2] 
maaslar[3] 
maaslar[4] 

for maas in maaslar:
    print(maas)

# dongu ve fonksiyonları birlikte kullanmak

def kare_al(x):
    print(x**2) 
    
kare_al(2)    

maaslar = [1000,2000,3000,4000,5000] 

for i in maaslar:
    print(i) 
    
# maaslara yuzde 20 zam yapilacak gerekli kodlari yaziniz.


1000*20/100  + 1000   

maaslar[0]*20/100 + maaslar[0] 
maaslar[1]*20/100 + maaslar[1] 
maaslar[2]*20/100 + maaslar[2]     
    
# dongu yazilacak   
# fonksiyon yazmak 
    
def yeni_maas(x): 
    print(x) 
    
yeni_maas(4) 

def yeni_maas(x):
    print(x*20/100 + x) 
    
yeni_maas(1000) 
yeni_maas(2000) 
yeni_maas(3000) 


for i in maaslar:
    yeni_maas(i) 
    
# mini uygulama
# if, for ve fonksiyonlari birlikte kullanmak    

    
maaslar = [1000,2000,3000,4000,5000] 

def maas_ust(x):
    print(x*10/100 + x) 

def maas_alt(x):
    print(x*20/100 + x) 

for i in maaslar:
    if i >= 3000:
        maas_ust(i) 
    else:
        maas_alt(i) 
        
        
# break & continue
        
maaslar = [8000,5000,2000,1000,3000, 7000, 1000] 

dir(maaslar) 

maaslar.sort() 
maaslar 

for i in maaslar:
    if i == 3000:
        print("kesildi") 
        break
    print(i) 

 

for i in maaslar:
    if i == 3000:
        continue
    print(i)

# while

sayi = 1

while sayi < 10:
    sayi += 1
    print(sayi)

