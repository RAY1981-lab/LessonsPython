from random import randint
print('Программа сортировки массива 20-ти чисел, заполненными случайными числами от -20 до 20')
numbers = []  # создаём массив numbers
for i in range(20):
    numbers.append(randint(-20, 20))



print(numbers)
