# NESNE YONELIMLI PROGRAMLAMA

# Sinif Nedir? : 
#  Benzer özellikler, ortak amaçlar taşıyan içerisinde fonksiyon ve değişkenler olan yapılardır.     

# Sinif Ozellikleri (Class attributes)

class VeriBilimci(): 
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []
    
# Siniflarin ozelliklerine erismek

VeriBilimci.bolum 
VeriBilimci.sql 

# siniflarin ozelliklerini degistirmek

VeriBilimci.sql = "Hayir"
VeriBilimci.sql

# Sinif Orneklendirmesi (instantiation)

ali = VeriBilimci() 

ali.sql 
ali.deneyim_yili 
ali.bolum 
ali.bildigi_diller.append("Python") 
ali.bildigi_diller 

veli = VeriBilimci() 
veli.sql 

veli.bildigi_diller 

# Ornek ozellikleri

class VeriBilimci():
    bildigi_diller = ["R","PYTHON"]
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''

ali = VeriBilimci() 
ali.bildigi_diller 

veli = VeriBilimci() 
veli.bildigi_diller 

ali.bildigi_diller.append("Python") 
ali.bildigi_diller 

veli.bildigi_diller 
veli.bildigi_diller.append("R") 
veli.bildigi_diller 

VeriBilimci.bildigi_diller 
ali.bolum  

VeriBilimci.bolum 
ali.bolum = "istatistik" 
VeriBilimci.bolum  
veli.bolum 
veli.bolum = "bil_muh"  
veli.bolum  
ali.bolum  
VeriBilimci.bolum 

# Ornek Metodlari

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil) :
        self.bildigi_diller.append(yeni_dil)


ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

dir(VeriBilimci)

VeriBilimci.dil_ekle
VeriBilimci.dil_ekle("R")

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller

# Miras Yapilari (inheritance)

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""

class DataScience(Employees):
    def __init__(self):
        self.Programming = ""

veribilimci1 = DataScience()
# veribilimci1.

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()
#mar1.


class Employee_yeni():
    def __init__(self, FirstName,LastName,Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address


ali = Employee_yeni("a","b","c")
ali.FirstName




# Python'da Fonksiyonel Programlama

# Fonksiyonlar dilin bastacidir. 
# (Birinci sinif nesnelerdir)
# Yan etkisiz fonksiyonlar. (stateless, girdi-cikti)
# Yuksek seviye fonksiyonlar.
# Vektorel operasyonlar.


# Yan Etkisiz Fonksiyonlar (Pure Functions)

# Ornek1:Bagimsizlik

A = 9

def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b


impure_sum(6)
pure_sum(3,4)



# Ornek2: Olumcul yan etkiler
# OOP
class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []
    
    def read(self):
        self.lines = [line for line in self.file]
    
    def count(self):
        return len(self.lines)


lc = LineCounter('deneme.txt') 

print(lc.lines) 
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())

#FP

def read(filename):
  with open(filename, 'r') as f:
      return [line for line in f]

def count(lines):
  return len(lines)

example_lines = read('deneme.txt')
lines_count = count(example_lines)
lines_count







# Vektorel Operasyonlar (Vectorel Operations)
# OOP
a = [1,2,3,4]
b = [2,3,4,5]

ab = []

range(0, len(a))

for i in range(0, len(a)):
    ab.append(a[i]*b[i])

ab

# FP

import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b



# Isimsiz Fonksiyonlar (Anonymous Functions)


def old_sum(a,b):
    return a + b

old_sum(4,5)


new_sum = lambda a,b: a + b
new_sum(4,5)


sirasiz_liste = [('b', 3), ('a', 8), ('d', 12), ('c', 1)]
sirasiz_liste

sorted(sirasiz_liste, key = lambda x: x[1])


# map & filter & reduce 

liste = [1,2,3,4,5]

for i in liste:
    print(i+ 10)


list(map(lambda x: x*10, liste))

# filter

liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x % 2 == 0, liste))

# reduce

from functools import reduce

liste = [1,2,3,4]
reduce(lambda a,b: a + b, liste)

# Modul Olusturmak


#HesapModulu.py
def yeni_maas(x):
    print(x*20/100 + x)
    
maaslar = [1000,2000,3000,4000]  


# test
import HesapModulu 
HesapModulu.yeni_maas(1000)


import HesapModulu as hm
hm.yeni_maas(2000)

from HesapModulu import yeni_maas
yeni_maas(3000)

import HesapModulu as hm
hm.maaslar

# Hatalar / istisnalar (exceptions)

# ZeroDivisionError hatasi
a = 10
b = 0

a/b


try:
    print(a/b)
except ZeroDivisionError:
    print("Payda da sifir olmaz")


# tip hatasi
    
a = 10    
b = "2"

a / b

try:
    print(a/b)
except TypeError:
    print("Sayi ve string problemi")




a = 10    
b = 2

a / b

try:
    print(a/b)
except TypeError:
    print("Sayi ve string problemi")



a = [13, 10, 15, 12, 17, 12, 19, 18, 11, 12, 190]
a.sort()
a


a
import numpy as np
np.median(a)
