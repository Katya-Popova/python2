



# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
n = int(input())
y = 0
x = 0
some_list = []
for i in range(1, n+1):
    y = ((1+1/i)**i)
    some_list.append(y)
    x = x+y
print(some_list)
print('Сумма:', x)

# Реализуйте алгоритм перемешивания списка
import random
some_list = [1, 5, 'erag', 54, 6]
random.shuffle(some_list)
print(some_list)
