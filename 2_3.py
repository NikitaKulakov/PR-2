# -*- coding: utf-8 -*-
n=int(input('Введите число минут: '))
n=n%(24*60)
m=n%60
c=n//60
print(c,'часов(-а)',m,'минут(-ы)')
