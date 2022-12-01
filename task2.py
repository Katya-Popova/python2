# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
x = int(input())
some_list=[]
count = 1
for i in range(1,x+1):
    count *= i
    some_list.append(count)
print(some_list)