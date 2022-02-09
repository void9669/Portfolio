"""Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно и не стоит
спать более B часов. Сейчас Аня спит Hчасов в сутки.
Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
Если Аня спит менее A часов, выведите “Недосып”, если же более B B B часов, то выведите “Пересып”."""
a = int(input())
b = int(input())
h = int(input())
if h < a:
    print('Недосып')
if h > b:
    print('Пересып')
if a <= h <= b:
    print('Это нормально')

# Требуется определить, является ли данный год високосным.

x = int(input('Введите год '))

if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
    print('Високосный')
else:
    print('Обычный')

# напишите программу, вычисляющую площадь треугольника по переданным длинам трёх его сторон по формуле Герона.

a = int(input('Enter value A'))
b = int(input('Enter value B'))
c = int(input('Enter value C'))

p = (a + b + c) / 2

s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

if (a + b) or (b + c) or (a + c) == 0:
    print('Impossible')
else:
    print(s)

'''Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в интервал
(−15,12]∪(14,17)∪[19,+∞)
и False в противном случае'''

x = int(input())
print((-15 < x <= 12) or (14 < x < 17) or (19 <= x))

'''Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию,
 после чего применяет операцию к введённым числам и выводит результат на экран.'''

x = float(input())
y = float(input())
z = input()

if z == '+':
    print(x + y)
elif z == '-':
    print(x - y)
elif z == '/':
    if y == 0:
        print("Деление на 0!")
    else:
        print(x / y)
elif z == '*':
    print(x * y)
elif z == 'mod':
    if y == 0:
        print("Деление на 0!")
    else:
        print(x % y)
elif z == 'pow':
    print(x ** y)
elif z == 'div':
    if y == 0:
        print("Деление на 0!")
    else:
        print(x // y)
'''написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры, 
которая бы выводила площадь получившейся комнаты.'''

z = input()

pi = 3.14

if z == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif z == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
elif z == 'круг':
    r = int(input())
    print(pi * r ** 2)
'''Напишите программу, которая получает на вход три целых числа, 
по одному числу в строке, и выводит на консоль в три строки сначала максимальное, 
потом минимальное, после чего оставшееся число.'''

a = int(input())
b = int(input())
c = int(input())
s = a + b + c
print(max(a, b, c))
print(min(a, b, c))
print(s - max(a, b, c) - min(a, b, c))

'''Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное),
 выводящее это число в консоль вместе с правильным образом изменённым словом "программист",
  для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.'''

n = int(input())

mod10 = n % 10
mod100 = n % 100

if mod10 == 1 and mod100 != 11:
    end = ''
elif (1 < mod10 < 5) and not (11 < mod100 < 15):
    end = 'а'
else:
    end = 'ов'

print(f'{n} программист{end}')

