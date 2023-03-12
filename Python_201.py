# LISTELER 

# iki sekilde gosterilebilirler 
# 1) []
# 2) list () 

notlar = [ 90, 56, 48, 99]
type(notlar)


liste = [ 'a', 22.9 , 1499]

liste_genis = [ 'a', 22.9 , 1499 , notlar]

len(liste_genis)

#-----------------------------------------------------------------

# Liste ici tip sorgulama

type(liste_genis[2])

#-----------------------------------------------------------------

# iki liste birlestirme

tum_liste = [ liste , liste_genis]

#-----------------------------------------------------------------

# olusturulan listeyi silme 

# del tum_liste     => Basina # koyulmali cunku program sonra calisinca hata vermesin

#-----------------------------------------------------------------

# Liste elemanlarina erismek 

liste[1]

liste[2]

liste[ 0:2 ]

liste[ :2 ]

liste[ 2: ]

yeni_liste = [ 'a',  10, [20 , 30 ,40 ,50 ]]

yeni_liste[1]

yeni_liste[0]

yeni_liste[ 0:2 ]

yeni_liste[2][1]

#-----------------------------------------------------------------

# Listelere Eleman Ekleme ile Degistirme ve Silme

# Elemean Degistirme

Liste = [ 'Ramazan', 'Ali', 'Veli', 'Osman']
Liste

# Ramazan olan degeri degistirelim 

Liste[0] = "Ahmet"
Liste

# Listedeki ilk 3 elemani degistirme

Liste[ 0:3 ] = "Ahmetin_babasi", "Alinin_babasi", "Velinin_babasi", 
Liste


Liste = [ 'Ahmet', 'Ali', 'Veli', 'Osman']
Liste

# Eleman Ekleme

Liste + ['Ayse']     #  =>  Bu sekilde yazarsak alttaki liste calisinca eklenmis sekilde cikti verir.
Liste

Liste = Liste + ['Ayse']    # => Seklinde yazarsak listeye kalici eklemis olduk.
Liste

# Eleman Silme

del Liste[2]         # Listeden Veliyi silmis olduk. Sildikten sonra # isareti koymayi unutma!!!!
Liste

#-----------------------------------------------------------------

# Metodlar ile Eleman Ekleme ve Silme: append() ve remove()

liste = [ 'A1', 'A2', 'A3']

liste 

liste.append('B1')

liste 

liste.remove('A2') 
liste 

#-----------------------------------------------------------------

# Indekslere Gore Eleman Ekleme ve Silme: insert() ve pop() 

liste = [ '3', '7', '9'] 

liste 

liste.insert(1, 'selam') 

liste 

liste.pop(0) 

liste 

#-----------------------------------------------------------------

# Diger Liste Metodlari

# count = Sayma fonksiyonudur. Listede bir elemandan kac tane var onu gosterir.

liste = [ 'Elma', 'Armut', 'Muz', 'Muz', 'Muz', 'Armut', 'Kivi' ] 

liste 

liste.count("Elma")  

liste.count("Muz")

liste.count("Armut") 

liste.count("Kivi") 

liste_yedek = liste.copy() # Elimizdeki mevcut listeyi kopyaladi

liste.extend( "a" ) 

liste 

liste.index("Kivi") # Elemanin kacinci indexte oldugunu gosterir

liste.reverse()  # Reverse + liste seklinde yazilirsa listeyi ters ceviriyor.
liste 

liste = [ '7', '2', '9', '39', '5', '1' ] 

liste 

liste.sort() # Onlar basamagina gore kucukten buyuge siraliyor

liste 

liste.clear() # Listeyi temizler

liste 

#-----------------------------------------------------------------

# TUPPLE 

# Kapsayicidirlar, Siralidirlar ve DEGISTIRILEMEZER !!!!

# Tupple Olusturma 

t = ( "ali", "veli", 1, 2, 3, 4, 5, [ 1, 5, 7, 6, 9]) # Bu ve alttaki gibi olusturulabilir

t = "ali", "veli", 1, 2, 3, 4, 5, [ 1, 5, 7, 6, 9 ] 

t = ( "eleman",)  # Onemli not: Burdaki "," isareti tek elemanli tupple'a ozeldir.

t = ( "eleman" )  # Burdaki gibi "," olmazsa burdaki t'nin type'i str olur.

# Tupplede eleman islemleri yapilamaz cunku tupplelar degistirilemez !!!!!

#-----------------------------------------------------------------

# Dictonarys( Sozlukler)

# Kapsayicidirlar, Sirasizdirlar ve Degistirilebilirler. 

# Sozluk Olusturma

sozluk = { "REG" : "REGRESYON MODELI", 
          "LOJ" : "LOJISTIC REGRESYON",
          "CART" : "CLASSIFICATION AND REG"}

sozluk 

len(sozluk) 

#-----------------------------------------------------------------

# Sozluk Eleman Secme Islemleri 

sozluk = { "REG" : "REGRESYON MODELI", 
          "LOJ" : "LOJISTIC REGRESYON",
          "CART" : "CLASSIFICATION AND REG"}

sozluk["REG"] 

sozluk["LOJ"] 


sozluk = { "REG" : ["REGRESYON MODELI", 10],
          "LOJ" : ["LOJISTIC REGRESYON", 20], 
          "CART" : ["CLASSIFICATION AND REG", 30] } 

sozluk["REG"] 

#-----------------------------------------------------------------

# Eleman Ekleme ve Degistirme

sozluk = { "REG" : "REGRESYON MODELI", 
           "LOJ" : "LOJISTIC REGRESYON",
           "CART" : "CLASSIFICATION AND REG"} 

sozluk[ "GBM" ] = "Gradient Boosting Mac"       # eleman ekleme

sozluk      

sozluk[ "REG" ] = "Coklu Dogrusal Regresyon "   # eleman degistirme

sozluk 

l = [1] 

l 

# sozluk [l] = "yeni bir sey " # burda hata verme nedeni listelerin degistirilebilen veri yapisi olmasi.

t = ("tupple",) 

t 

sozluk[t] = "yeni bir sey"  # burda hata vermedi cunku tupple sabit veri yapilidir.

sozluk 

#-----------------------------------------------------------------

# SETLER (KUMELER) 

# Sirasizdirlar, Degerleri essizdirler, Degistirilebilirler ve Farkli tipleri Barindirabilirler.

# Set Olusturma 

s = set () 

s 

L = [ 1, "a ", "ali", 135 ]   # Liste 

s = set(L)  


t = ( "a", "ali" )  #tupple

s = set(t) 


L = [ "ali", "Lutfen", "ata", "bakma", "uzaya", "git", "git", "ali", "git" ] 

s = set(L) 

s       # Setler 1'den cok tekrar eden karakterleri bir kere yazar. 

len(s) 

s [0]  # TypeError verdi. Cunku setler sirasiz indekslerdir. 

#-----------------------------------------------------------------

# Eleman Ekleme ve Cikarma

L = [ "gelecegi", "yazanlar" ] 

s = set(L) 

s 

s.add("ile")        # Ekleme

s 

s.remove("yazanlar")        # Silme 

s 

s.discard("merhaba")  # hata vermeden kontrol eder. 

# -----------------------------------------------------------------

#Setler - Klasik Kume Islemleri

# =============================================================================
# difference() ile iki kumenin farkini ya da "-" ifadesi
# intersection() iki kume kesisimi ya da "&" ifadesi
# union() iki kumenin birlesimi
# symmetric_difference() ikisinde de olmayanlari.
# =============================================================================


#difference

set1 = set([1,3,5]) 
set2 = set([1,2,3]) 

set1.difference(set2) 

set2.difference(set1) 

set1.symmetric_difference(set2) 

set1 - set2 
set2 - set1 

#intersection & union

set1 = set([1,3,5]) 
set2 = set([1,2,3]) 

set1.intersection(set2) 
set2.intersection(set1) 


kesisim = set1 & set2 
kesisim 

birlesim = set1.union(set2) 
birlesim 

set1.intersection_update(set2) 
set1 


#Set Sorgu Islemleri

set1 = set([7,8,9]) 
set2 = set([5,6,7,8,9,10]) 

#iki kumenin kesisiminin bos olup olmadiginin sorgulanmasi 

set1.isdisjoint(set2) 


#bir kumenin butun elemanlarinin baska bir kume icerisinde yer alip almadigi

set1.issubset(set2) 

#bir kumenin bir diger kumeyi kapsayip kapsamadigi

set2.issuperset(set1) 




