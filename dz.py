# import random
# x = random.randint(1, 100)  # Случайное целое число от 1 до 100
# #
# # while True:
# #     print("Попробуй угадать число")
# #     z = int(input("Введи число:  "))
# #     if z<x:
# #         print("Слишком маленькое число")
# #     elif z>x:
# #         print("Слишком большое число")
# #     else:
# #         print("Молодец поздравлю")
# #         break
#
# # Создать алгоритм, который проходится по списку и выводит числа с индексом кратно 5
#
# # n = [
# #     'Toyota Camry', 'Honda Civic', 'BMW X5', 'Mercedes-Benz E-Class',
# #     'Audi A4', 'Ford Focus', 'Volkswagen Golf', 'Hyundai Solaris',
# #     'Kia Rio', 'Lada Vesta'
# # ]
#
# # for car in n:
# #     print(car)
# #     # print("            " + str(len(car)) + "  simbols")
# #     print("            ", len(car), "simbols", sep="тчк", end="%")
# #     if len(car) <= 12:
# #         print("Название помещается на маленький экран")
# #     else:
# #         print("Название не помещается на маленький экран")
# #     print()
#
# print(list(range(1,10,2)))
from itertools import count

# # Напишите программу, которая выводит числа от 1 до 10 с помощью while
# l=1
# while l<=10:
#     print (l)
#     l+=1

# Программа, которая суммирует числа, вводимые пользователем, пока не будет введен 0
#

# total = 0
# while True:
#     num = int(input("Введите число: "))
#     if num == 0:
#         break
#     total += num
# print(f"Сумма всех введенных чисел: {total}")

# # Напишите программу, которая выводит все четные числа от 2 до 20
# l=2
# x = int(input("введите число: "))
# while l <=x:
#     print(l)
#     l+=2
#
# Программа, которая запрашивает пароль до тех пор, пока не будет введен правильный
# password = 8877
# while True:
#     num = int(input("Введите пароль: "))
#     if num == password:
#         break
# print("Верный пароль")
# Напишите обратный отсчет от 10 до 1 с выводом "Пуск!"

num=10
while num >=1:
    print(num)
    num -=1
