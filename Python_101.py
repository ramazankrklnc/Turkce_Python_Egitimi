# GENELLER PYTHON NOTLARI
#-----------------------------------------------------------------
# NUMBERS AND CHARACTERS INFORMATION (NUMARA VE KARAKTER BILGILERI)
#-----------------------------------------------------------------
# Sayilar integer ve float olarak ikiye ayrilir. int= tam sayilari;
# float= ondalikli yani kesirlileri gosterir. 
# Stringler(Karakter Dizinleri)= Cift tirnak veya tek tirnak kullanilir. 
# "type()" fonksiyonu bize parantez icine girilen her seyin turunu gosterir.
# "print()" fonksiyonu bizim ekrana yazdir fonksiyonumuzdur.

print("Merhabalar")


type(9)

type(12.6)

type("R")

type("Merhabalar")

#-----------------------------------------------------------------

# STRINGS CLOSER LOOK (STRINGLERE YAKINDAN BAKMAK) 
# " " kullandigimizda python str olarak algiliyor

"123"
type("123")

#-----------------------------------------------------------------
# iki str ifadesini bir araya getirmek

"a" + "-b" # ( buradaki + isareti toplama anlaminda degildir. ) 
"a" " b" # veya bu sekilde de olabilir.

# str ifadesini cogaltmak

"a "*7

#------------------------------------------------------------------
# UZUNLUK (ELEMAN SAYISI) BILGISINE ERISMEK = len() FONSIYONU
# Metodlar veri veya belili yapilar uzerine uygulanan cesitli fonsiyonlardir.

pyt_org = "python_ogreniyorum"

# onceki w hala degisken tablosunda duruyor onu silmek icin sag tiklayip remove
# veya asagiya yazacagim gibi kod silme komutu da oluyor
# del w silme islemi bittikten sonra diyez isareti ile yorum satiri yapiyoruz.

a = 10
b = 215

a*b

len(pyt_org)
len("python_ogreniyorum")

#------------------------------------------------------------------
# BUYUK-KUCUK HARF DONUSUMLERI = upper() &lower()  FONSIYONU

pyt_org = "python_ogreniyorum"

pyt_org.upper() # buyuk harflerle

pyt_org.lower() # kucuk harflerle

pyt_org.islower()
B = pyt_org.upper()

pyt_org.isupper()

B.isupper()

B.islower()


#------------------------------------------------------------------
# KARAKTER DEGISTIRME = replace() FONSIYONU
# harf degistirmeye yarar. Ornegin e'leri a yapalim.

pyt_org.replace("e", "a")

pyt_org.replace("a", "e")


#------------------------------------------------------------------
# KARAKTER KIRPMA = strip() FONSIYONU
# istenmeyen karakterleri kirpmak icin kullanilir
# Orengin asagidakinin kenarlarindaki cizgileri yok edelim.

pyt_org = " _python_ogreniyorum_ "

pyt_org.strip("_")


#------------------------------------------------------------------
#SUBSTRINGLER
gel_yaz = "gelecegi_yazanlar"

gel_yaz[1] 

gel_yaz[15]

gel_yaz[0:5] # 0'dan basla 5'e kadar anlaminda

gel_yaz[3:11] 



#------------------------------------------------------------------
#DEGISKENLER

A = 99
b =  "ali_uzaya_git" 
C = A/3

A/C

A*C

A*5


#------------------------------------------------------------------
# TYPE DONUSUMLERI

toplama_bir = input()
toplama_iki = input()


toplama_bir + toplama_iki #Burda ikisi de str deger oldugu icin yan yana yazdi yani birlestirdi. 

int(toplama_bir) + int(toplama_iki)

10.0    # float degeri int donusturme;

type(10.0)
int(10.0)


12      # int degeri float'a donusturme;

type(12)
float(12)



#------------------------------------------------------------------
#-print() Fonksiyonu = Ekrana yazdirmaya yariyor

print("gelecegi" , "yazanlar")

print("gelecegi" , "yazanlar" , sep= "_") # sep fonk birlestirmeye yariyor.  

