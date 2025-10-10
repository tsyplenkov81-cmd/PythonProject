# Оценка соответствия кандидата стандартам
# 1-100, 1- не подходит, а 100 - полностью подходит
# возраст, образование, опыт, пол, военный билет, семейное положение
# возраст до 18, от 65 нельзя,
# образование: да, нет, не оконченное (20, 0, 10)
# опыт нет, 10, 20, 30 (0, 5, 10, 20)
# пол м / ж
# если м и военник есть то 20, если нет 0, и у ж семейное положение да 20 нет 0
woman = 0
man = 0
user_name = input("Введите имя:  ")
user_age = int(input("Укажите свой возраст:  "))
if user_age<18 or user_age>65:
    print ("Данный сервис Вам не доступен")
    exit()
user_educ = int(input("""Какое у вас образование:
 1-высшее образование
 2-неоконченное
 3-нет образование
 укажите  """))
if user_educ == 1:
    educ = 20
if user_educ == 2:
    educ = 10
if user_educ == 3:
    educ = 10
user_experience = int(input("""Укажите свой опыт в професии:
1 - опыта нет
2 - стаж более 5 лет
3 - стаж более 10 лет
4 - стаж более 20 лет
укажите  """))
if user_experience == 1:
    experience = 0
if user_experience == 2:
    experience = 5
if user_experience == 3:
    experience = 10
if user_experience == 4:
    experience = 20
user_gender = input("""Укажите пол в формате М или Ж
укажите """)
if user_gender == "М":
    gender = int(input ("""Есть ли у вас военный билет
    1 - если есть
    2 - если нет
    укажите  """))
    if gender == 1:
        man = 20
    if gender == 2:
        man = 0
if user_gender == "Ж":
    gender = int(input ("""Состоите ли в браке
    1 - если да
    2 - если нет
    укажите  """))
    if gender == 1:
        woman = 20
    if gender == 2:
        woman = 0

print("Итоговое значение: ", educ + experience + experience + man + woman)
# расчет итогового значения
# максимальное значение 80 мин 0
# user_age + user_educ + user_experience + user_gender = itog
#itog = (educ + experience + experience + woman + man)
#print(itog)