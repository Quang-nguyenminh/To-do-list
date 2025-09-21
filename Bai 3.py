# name = str(input('Insert name: '))
# math = float(input('Insert Math score: '))
# literature = float(input('Insert Literature score: '))
# english = float(input('Insert English score: '))
# average = (math + literature + english) /3
#
# print('Name:', name, '\n', 'Average score:', average)
#
# if average >= 9:
#     print('Grade: High Distinction')
# elif average >= 8:
#     print('Grade: Distinction')
# elif average >= 6.5:
#     print('Grade: Good')
# elif average >= 5:
#     print('Grade: Average')
# else:
#     print('Grade: Poor')
# ---------------------------------------------------------------------

# Find x from: ax + b = 0
# a = float(input('Insert number a: '))
# b = float(input('Insert number b: '))
# if b == 0:
#     if a == 0:
#         x = 'Every value is possible'
#     else:
#         x = 0
# else:
#     if a == 0:
#         x = 'No value is possible'
#     else:
#         x = (-b)/a
# print(x)
# --------------------------------------------------------------------------------
#
# a = float(input('Insert number a: '))
# b = float(input('Insert number b: '))
# c = float(input('Insert number c: '))
# d = float(input('Insert number d: '))
#
# max = a
#
# if b > max:
#     max = b
# if c > max:
#     max = c
# if d > max:
#     max = d
#
# print(max)
#
# print(max(a, b, c, d))
# ---------------------------------------------------------------------------------------

# Find x in: a*x^2 + b*x + c = 0
import math

a = float(input('Insert number a: '))
b = float(input('Insert number b: '))
c = float(input('Insert number c: '))
delta = b*b - 4*a*c

if delta < 0:
    print('No value x is possible.')
elif delta == 0:
    print('x = ', (-b)/(2*a))
else:
    print('x1 = ', (-b-math.sqrt(delta))/(2*a), '\n', 'x2 = ', (-b+math.sqrt(delta))/(2*a))
