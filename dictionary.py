# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 09:17:22 2025

@author: Zavharbek
"""

#Dictionary (Lug'at)

car_0 ={'model':'ferrare', 'rang':'qizil'}
#print(car_0['model'])
#print(car_0['rang'])

eng_uz = {'apple': 'olma','apricot':"o'rik", 'banana':"banan"}
print(eng_uz['apple'])

mevalar = {'olma': 10000, 'tarvuz':8000, 'qovun': 10000}
# print(f"Olma narxi {mevalar['olma']}") 

talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(f"{talaba_0['ism'].title()},\
 {talaba_0['t_yil']}-yilda tu'gilgan,\
 {talaba_0['yosh']} yoshda")
 
talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika' 
print(talaba_0)
#Bo'sh lug'at yaratish
talaba_1 = {}

#Yangi qiymatlar qo'shish
talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

#Qiymatlarni o'zgartirish
talaba_1['kurs'] = 4 # 'kurs' ni 4 ga o'zgartiramiz.
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

#Lug'atni qatorlarga bo'lib yozish
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

#get() metodi
phone = telefonlar['ali']
print(f"Alining telefoni {phone}")

# phone = telefonlar['hasan']
# print(f"Hasanning telefoni {phone}")

phone = telefonlar.get('hasan','Bunday ism mavjud emas')
print(phone)

# phone = telefonlar.get('hasan')
# print(phone)

