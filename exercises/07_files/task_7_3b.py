# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
number = input('Введите номер vlan: ')
result = []
with open('CAM_table.txt') as f:
    for line in f:
        if line =='\n':
            pass
        elif ((line.split())[0]).isdigit():
            line = line.split()
            result.append(line)
    for i in range(len(result)):
        if number == result[i][0]:
            print('{:<9}{:20}{:9}'.format(result[i][0], result[i][1], result[i][3]))