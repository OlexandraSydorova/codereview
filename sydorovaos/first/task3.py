"""Знайти суму цілих чисел із діапазону дійсних чисел"""
first = float(input())
last = float(input())
sum = 0
for i in range(int(first+1),int(last+1)):
    sum+=i
print(sum)