# string = input('Input string: ')
# length = len(string)
# if length % 2 == 1:
#     print(string[length//2])
# else:
#     print(string[length//2 - 1: length//2 + 1])
# ----------------------------------------------------------------------------------------
b_d = int(input('Input day: '))
b_m = int(input('Input month: '))
b_y = int(input('Input year: '))

from datetime import datetime
now = datetime.now()
current_day = int(now.strftime('%d'))
current_month = int(now.strftime('%m'))
current_year = int(now.strftime('%Y'))

y = current_year - b_y
if current_month - b_m < 0:
    y -= 1
elif current_month - b_m == 0:
    if current_day - b_d < 0:
        y -= 1
print(y)