# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

with open('config_sw1.txt') as f:
    for line in f:
        g = False
        for ig in ignore:
            if ig in line:
                g = True
                break
        if line.startswith('!'):
            pass
        elif line.startswith(' ') and g == False:
            print(' ' + line.strip())
        elif g == False:
            print(line.strip())