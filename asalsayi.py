# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:42:43 2024

@author: asus
"""

sayi = int(input("sayı giriniz"))
asalmi = True
for x in range(2,sayi):
    if (sayi % x) == 0:
        asalmi = False
        break
if asalmi == True:
    print("asaldır")
else:
    print("asal değil")