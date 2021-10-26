# -*- coding: utf-8 -*-
n = int(input('Введите натуральное число: '))
def F(n):
  if ((n % 4 ==0) and (n % 100 !=0)) or (n % 400 ==0):
    return'Да,', n ,'високосный год'
  else:
      return'Нет,', n ,'не високосный год'
print(F(n))
