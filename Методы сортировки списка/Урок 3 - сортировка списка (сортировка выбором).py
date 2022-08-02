from random import randint
print('Программа сортировки списка из 20-ти чисел, заполненными случайными числами от -20 до 20')
numbers = []  # создаём список numbers
for i in range(20):  # цикл заполнения 20-ти элементов списка
    numbers.append(randint(-20, 20))  # добавляем (append) случайные числа от -20 до 20 в numbers
print('Начальный неотсортированный список: ', numbers)  # Выводим заполненный неотсортированный список

for i in range(0, len(numbers)):  # цикл перебора от 0 до длины списка
    for n in range(i+1, len(numbers)):  # цикл перебора от 1 до длины списка
        if (numbers[n] < numbers[i]):  # условие
            numbers[n], numbers[i] = numbers[i], numbers[n]  # меняем местами [n] и [i] в списке numbers

print("Отсортированный список: ", numbers)  # выводим уже отсортированный список в консоль
