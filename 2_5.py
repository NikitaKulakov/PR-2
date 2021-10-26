# -*- coding: utf-8 -*-
a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
c=int(input('Введите третье число: '))
def f(a,b,c):
  if (a < c) and (a < b):
    return a
  elif b < c: return b
  else: return c
print(f(a,b,c))
