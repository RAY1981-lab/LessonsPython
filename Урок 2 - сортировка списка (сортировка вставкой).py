from random import randint
print('Программа сортировки списка из 20-ти чисел, заполненными случайными числами от -20 до 20')
numbers = []  # создаём список numbers
for i in range(20):  # цикл заполнения 20-ти элементов списка
    numbers.append(randint(-20, 20))  # добавляем (append) случайные числа от -20 до 20 в numbers
print('Начальный неотсортированный список: ', numbers)  # Выводим заполненный неотсортированный список

for i in range(1, len(numbers)):
    while (i > 0 and numbers[i] < numbers[i-1]):
        numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
        i -= 1
print("Отсортированный список: ", numbers)
