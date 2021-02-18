school = {'1А': 20, '1Б': 23, '2А': 15, '2Б': 29, '3А': 26, '3Б': 14}
children = 0
print(school)
print('Какое действие?')
print('1) изменение количества учащихся в классе')
print('2) добавление нового класса (с количеством учеников)')
print('3) удаление класса из базы')
print('4) подсчёт общего количества учеников в школе')
do = int(input('Введите номер действия:'))
if do == 4:
    children = sum(school.values())
    print(children)
elif do == 3:
    del_class = input('Какой класс удалить?')
    school.pop(del_class)
    print(school)
elif do == 2:
    new_class = input('Какой класс добавить? \n Введите класс:')
    count_children = input('Введите количество учеников:')
    school[new_class] = count_children
    print('Новый класс создан.')
    print(school)
elif do == 1:
    new_class = input('Какой класс изменить? \n Введите класс:')
    count_children = input('Количество учеников:')
    if new_class not in school:
        print('В школе нет такого класса!')
    else:
        school[new_class] = count_children
        print('Класс изменён!')
        print(school[new_class], count_children)
