# n = int(input('Insert an integer: '))
# S = 1
# i = 1
# for k in range(1, n+1):
#     S *= k
# while i < n+1:
#     S *= i
#     i += 1
# print(S)
# ---------------------------------------------------------------------------------------
# n = int(input('Insert an integer: '))
# i = 1
# count = 0
# while i <= n:
#     count += 1
#     i *= 10
# print(n, 'has', count, 'number in them.')
# -----------------------------------------------------------------------------------------
# n = int(input('Insert an integer from 0 to 100: '))
# g = int(input('Guess'))
# if while g != n:
# -----------------------------------------------------------------------------------------
# n = int(input('Insert an integer: '))
# F1 = 1
# F2 = 1
# f = 0
# i = 2
# while i <= n:
#     f = F1 + F2
#     F1 = F2
#     F2 = f
#     i += 1
# print(F1)
# ------------------------------------------------------------------------------------------
n = 200
i = 2
count = 0
while i <= n:
    for k in range(1, i+1):
        if i%k == 0:
            count +=1
    if count == 2:
        print(i, end = ' ')
    count = 0
    i += 1
