# Программа-игра. Нужно угадать число, загаданное компьютером
import random  # импортируем модуль "Import"
print('Игра: угадай число, которое загадал компьютер')
comp = random.randint(1, 100)  # Генерируем случайное целое число от 1 до 100 и помещаем его в переменную comp
print('Всё, я загадал число от 1 до 100. Посмотрим, с какой попытки Вы его угадаете! ))')
print(comp)  # Выводим число, загаданное компьютером (потом удалить, т.к. оно для разработчика)
popitka = 1  # переменная для хранения кол-ва попыток
user = 0  # переменная для ввода угадываемого числа
while user != comp:  # цикл: выполняется до тех пор, пока числа, загаданные компом и юзером, не совпадут
    user = int(input('Введите число: '))  # юзер вводит число
    if user > comp:
        print('Ваше число больше, загаданного компьютером')
        print('Использована ', popitka, '-я попытка')
        popitka = popitka + 1
    elif user < comp:
        print('Ваше число меньше, загаданного компьютером')
        print('Использована ', popitka, '-я попытка')
        popitka = popitka + 1
    else:
        print("Вы угадали это число с ", popitka, ' попытки! Кросаучек!')